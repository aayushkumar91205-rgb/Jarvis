import json
import os
from datetime import datetime

USERS_FILE = "users.json"
MEMORY_FILE = "jarvis_memory.txt"

DEFAULT_MEMORY = """You are Jarvis, an advanced AI assistant created by Aayush."""

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {
        "Aayush": {
            "password": "123098",
            "role": "admin",
            "school": "Aayush Technology ",
            "title_pref": "Sir",
            "name": "Aayush",
            "class": "10",
            "email": "example@gmail.com"
        }
    }

def save_users(users_data):
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users_data, f, indent=4)
    except Exception:
        pass

def add_or_update_detailed_user(username, password, role, details):
    users = load_users()
    users[username] = {
        "password": password,
        "role": role,
        "school": details.get("school", "Aayush Technology High"),
        "title_pref": details.get("title_pref", "Sir"),
        "name": details.get("name", username),
        "class": details.get("class", "10"),
        "email": details.get("email", "")
    }
    save_users(users)

def delete_user(username):
    users = load_users()
    if username in users and username != "Aayush":
        del users[username]
        save_users(users)

def change_password(username, new_password):
    users = load_users()
    if username in users:
        users[username]["password"] = new_password
        save_users(users)

def get_jarvis_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            return DEFAULT_MEMORY
    else:
        save_jarvis_memory(DEFAULT_MEMORY)
        return DEFAULT_MEMORY

def save_jarvis_memory(content):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception:
        pass

def load_permanent_memory():
    return get_jarvis_memory()

def auto_save_memory(text):
    save_jarvis_memory(text)

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")
