import json
import uuid
import os

def load_json(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def generate_id():
    return str(uuid.uuid4())

def validate_phone(phone):
    return phone.startswith("+234") and phone[4:].isdigit() and len(phone) == 14 or (
        phone.startswith("0") and phone[1:].isdigit() and len(phone) == 11
    )

def validate_nin(nin):
    return nin.isdigit() and len(nin) == 11

def title_case(text):
    return text.title().strip()
