import unittest
from app.main import _normalise_event, _stats
from decimal import Decimal


class EventValidationTests(unittest.TestCase):
    def test_valid_occupancy(self):
        item = _normalise_event({
            "building": "Library-A", "room": "A203",
            "event_type": "occupancy", "value": 42, "unit": "people"
        })
        self.assertEqual(item["event_type"], "occupancy")
        self.assertEqual(item["severity"], "normal")
        self.assertEqual(item["value"], Decimal("42"))

    def test_high_occupancy_alert(self):
        item = _normalise_event({
            "building": "Library-A", "room": "A203",
            "event_type": "occupancy", "value": 95, "unit": "people"
        })
        self.assertEqual(item["severity"], "alert")

    def test_missing_field_rejected(self):
        with self.assertRaises(ValueError):
            _normalise_event({"building": "Library-A", "event_type": "occupancy", "value": 42, "unit": "people"})

    def test_invalid_type_rejected(self):
        with self.assertRaises(ValueError):
            _normalise_event({
                "building": "Library-A", "room": "A203",
                "event_type": "unknown", "value": 2, "unit": "x"
            })

    def test_negative_occupancy_rejected(self):
        with self.assertRaises(ValueError):
            _normalise_event({
                "building": "Library-A", "room": "A203",
                "event_type": "occupancy", "value": -1, "unit": "people"
            })

    def test_stats_uses_latest_occupancy_per_room(self):
        events = [
            {"event_type": "occupancy", "building": "Library-A", "room": "A203",
             "value": Decimal("42"), "timestamp": "2026-10-09T10:00:00Z", "severity": "normal"},
            {"event_type": "occupancy", "building": "Library-A", "room": "A203",
             "value": Decimal("50"), "timestamp": "2026-10-09T11:00:00Z", "severity": "normal"},
            {"event_type": "energy", "value": Decimal("18.5"), "severity": "normal"},
        ]
        result = _stats(events)
        self.assertEqual(result["latest_occupancy_people"], 50)
        self.assertEqual(result["total_events"], 3)


if __name__ == "__main__":
    unittest.main()
