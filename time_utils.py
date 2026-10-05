import json
import os
from datetime import datetime, timezone, timedelta

TIMETABLE_FILE = "timetable.json"
IST = timezone(timedelta(hours=5, minutes=30))

def load_timetable():
    if os.path.exists(TIMETABLE_FILE):
        try:
            with open(TIMETABLE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return [
        {"time": "08:00 AM", "notify": "Yes", "message": "Morning Mathematics Study Session"},
        {"time": "04:00 PM", "notify": "Yes", "message": "Physics Practice Worksheet"}
    ]

def save_timetable(schedule_data):
    try:
        with open(TIMETABLE_FILE, "w", encoding="utf-8") as f:
            json.dump(schedule_data, f, indent=4)
    except Exception:
        pass

def check_and_trigger_timetable():
    current_time_str = datetime.now(IST).strftime("%I:%M %p")
    schedule = load_timetable()
    triggered = []
    for item in schedule:
        if item.get("time") == current_time_str and item.get("notify") == "Yes":
            triggered.append(item.get("message"))
    return triggered
