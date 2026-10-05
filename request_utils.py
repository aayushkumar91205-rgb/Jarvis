import json
import os

REQUESTS_FILE = "requests.json"

def load_requests():
    if os.path.exists(REQUESTS_FILE):
        try:
            with open(REQUESTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_request(req_data):
    reqs = load_requests()
    reqs.append(req_data)
    try:
        with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
            json.dump(reqs, f, indent=4)
    except Exception:
        pass

def delete_request(index):
    reqs = load_requests()
    if 0 <= index < len(reqs):
        reqs.pop(index)
        try:
            with open(REQUESTS_FILE, "w", encoding="utf-8") as f:
                json.dump(reqs, f, indent=4)
        except Exception:
            pass
