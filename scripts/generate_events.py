"""Send simulated campus events to a deployed CampusPulse API."""
import json
import os
import sys
import urllib.error
import urllib.request

BASE_URL = os.environ.get("CAMPUSPULSE_URL", "").rstrip("/")
TOKEN = os.environ.get("CAMPUSPULSE_ADMIN_TOKEN", "")

if not BASE_URL or not TOKEN:
    sys.exit("Set CAMPUSPULSE_URL and CAMPUSPULSE_ADMIN_TOKEN environment variables first.")

events = [
    {"building": "Library-A", "room": "A203", "event_type": "occupancy", "value": 42, "unit": "people"},
    {"building": "Engineering", "room": "Lab-02", "event_type": "energy", "value": 18.5, "unit": "kWh"},
    {"building": "Library-A", "room": "A203", "event_type": "occupancy", "value": 95, "unit": "people"},
    {"building": "Engineering", "room": "Lab-02", "event_type": "temperature", "value": 38, "unit": "C"},
]

for item in events:
    req = urllib.request.Request(
        BASE_URL + "/events",
        data=json.dumps(item).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + TOKEN},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            print(response.status, response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print("HTTP", exc.code, exc.read().decode("utf-8"))
        raise
