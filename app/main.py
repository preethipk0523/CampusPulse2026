
import json
import os
import uuid
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation

import boto3

TABLE_NAME = os.environ.get("EVENTS_TABLE", "CampusPulseEvents")
OPERATOR_PASSWORD = os.environ.get("OPERATOR_PASSWORD", "")
OPERATOR_TOKEN = os.environ.get("OPERATOR_TOKEN", "")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "")

ALLOWED_TYPES = {
    "occupancy",
    "energy",
    "temperature",
    "humidity",
    "maintenance",
}

_dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.environ.get(
        "AWS_REGION",
        os.environ.get("AWS_DEFAULT_REGION", "eu-west-3"),
    ),
)
_table = _dynamodb.Table(TABLE_NAME)


def _json_default(value):
    if isinstance(value, Decimal):
        if value == value.to_integral_value():
            return int(value)
        return float(value)

    raise TypeError(f"Unsupported type: {type(value).__name__}")


def _response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
        },
        "body": json.dumps(body, default=_json_default),
    }


def _body(event):
    raw = event.get("body")

    if not raw:
        return {}

    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        raise ValueError("Request body must be valid JSON")


def _role_for_token(token):
    if token and ADMIN_TOKEN and token == ADMIN_TOKEN:
        return "admin"

    if token and OPERATOR_TOKEN and token == OPERATOR_TOKEN:
        return "operator"

    return None


def _current_role(event):
    headers = {
        str(key).lower(): value
        for key, value in (event.get("headers") or {}).items()
    }

    authorization = headers.get("authorization", "")

    if not authorization.startswith("Bearer "):
        return None

    token = authorization[7:].strip()
    return _role_for_token(token)


def _normalise_event(data):
    required = [
        "building",
        "room",
        "event_type",
        "value",
        "unit",
    ]

    missing = [
        key
        for key in required
        if key not in data or data[key] in ("", None)
    ]

    if missing:
        raise ValueError(
            "Missing required fields: " + ", ".join(missing)
        )

    event_type = str(data["event_type"]).lower().strip()

    if event_type not in ALLOWED_TYPES:
        raise ValueError(
            "event_type must be one of: "
            + ", ".join(sorted(ALLOWED_TYPES))
        )

    try:
        value = Decimal(str(data["value"]))
    except (InvalidOperation, ValueError):
        raise ValueError("value must be numeric")

    if not value.is_finite():
        raise ValueError("value must be a finite number")

    if event_type in {"occupancy", "energy"} and value < 0:
        raise ValueError(f"{event_type} value cannot be negative")

    if event_type == "occupancy" and value != value.to_integral_value():
        raise ValueError("occupancy must be a whole number")

    if event_type == "occupancy" and value > 80:
        severity = "alert"
    elif event_type == "energy" and value > 50:
        severity = "alert"
    elif event_type == "temperature" and (
        value < 10 or value > 35
    ):
        severity = "alert"
    else:
        severity = "normal"

    timestamp = data.get("timestamp") or datetime.now(
        timezone.utc
    ).isoformat()

    return {
        "event_id": str(
            data.get("event_id") or f"evt-{uuid.uuid4()}"
        ),
        "building": str(data["building"]).strip(),
        "room": str(data["room"]).strip(),
        "event_type": event_type,
        "value": value,
        "unit": str(data["unit"]).strip(),
        "severity": severity,
        "timestamp": str(timestamp),
    }


def _all_events():
    # Scan is acceptable only for a small demonstration dataset.
    result = _table.scan()
    items = result.get("Items", [])

    while result.get("LastEvaluatedKey"):
        result = _table.scan(
            ExclusiveStartKey=result["LastEvaluatedKey"]
        )
        items.extend(result.get("Items", []))

    return sorted(
        items,
        key=lambda item: str(item.get("timestamp", "")),
        reverse=True,
    )


def _stats(events):
    latest_occupancy = {}
    energy_sum = Decimal("0")
    energy_count = 0

    for item in events:
        kind = item.get("event_type")

        try:
            value = Decimal(str(item.get("value", 0)))
        except (InvalidOperation, ValueError):
            continue

        if kind == "occupancy":
            key = (
                item.get("building", ""),
                item.get("room", ""),
            )
            timestamp = str(item.get("timestamp", ""))

            if (
                key not in latest_occupancy
                or timestamp > latest_occupancy[key][0]
            ):
                latest_occupancy[key] = (timestamp, value)

        elif kind == "energy":
            energy_sum += value
            energy_count += 1

    latest_occupancy_people = sum(
        (
            entry[1]
            for entry in latest_occupancy.values()
        ),
        Decimal("0"),
    )

    return {
        "total_events": len(events),
        "latest_occupancy_people": int(latest_occupancy_people),
        "energy_readings_count": energy_count,
        "sum_of_recorded_energy_values_kwh": energy_sum,
        "alert_count": sum(
            1
            for item in events
            if item.get("severity") in {"alert", "urgent"}
        ),
    }


def lambda_handler(event, context):
    path = event.get("path", "/")
    method = event.get("httpMethod", "GET").upper()

    if method == "OPTIONS":
        return _response(200, {"message": "CORS preflight"})

    # Public health check
    if path == "/health" and method == "GET":
        return _response(
            200,
            {
                "status": "ok",
                "service": "CampusPulse 2026",
            },
        )

    # Demo login
    if path == "/login" and method == "POST":
        try:
            data = _body(event)
        except ValueError as exc:
            return _response(400, {"error": str(exc)})

        role = data.get("role")
        password = data.get("password", "")

        if (
            role == "operator"
            and OPERATOR_PASSWORD
            and password == OPERATOR_PASSWORD
            and OPERATOR_TOKEN
        ):
            return _response(
                200,
                {
                    "role": "operator",
                    "token": OPERATOR_TOKEN,
                },
            )

        if (
            role == "admin"
            and ADMIN_PASSWORD
            and password == ADMIN_PASSWORD
            and ADMIN_TOKEN
        ):
            return _response(
                200,
                {
                    "role": "admin",
                    "token": ADMIN_TOKEN,
                },
            )

        return _response(401, {"error": "Invalid credentials"})

    # All remaining endpoints require a valid bearer token
    role = _current_role(event)

    if not role:
        return _response(
            401,
            {"error": "Bearer token required or invalid"},
        )

    # Admin-only event creation
    if path == "/events" and method == "POST":
        if role != "admin":
            return _response(
                403,
                {"error": "Admin role required to create events"},
            )

        try:
            data = _body(event)
            item = _normalise_event(data)
        except ValueError as exc:
            return _response(400, {"error": str(exc)})

        _table.put_item(Item=item)

        return _response(
            201,
            {
                "message": "Event stored",
                "event": item,
            },
        )

    # Retrieve events
    if path == "/events" and method == "GET":
        try:
            query = event.get("queryStringParameters") or {}
            limit = int(query.get("limit", "50"))
        except (ValueError, TypeError):
            return _response(
                400,
                {"error": "limit must be an integer"},
            )

        limit = max(1, min(limit, 100))

        return _response(
            200,
            {"events": _all_events()[:limit]},
        )

    # Statistics
    if path == "/stats" and method == "GET":
        return _response(200, _stats(_all_events()))

    # Alerts
    if path == "/alerts" and method == "GET":
        alerts = [
            item
            for item in _all_events()
            if item.get("severity") in {"alert", "urgent"}
        ]

        return _response(200, {"alerts": alerts})

    return _response(404, {"error": "Route not found"})
