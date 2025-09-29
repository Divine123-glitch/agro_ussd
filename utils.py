import json
import os
import uuid
import re

def load_json(file):
        try:
            if not os.path.exists(file):
                with open(file, "w") as f:
                    json.dump([], f)
            with open(file, "r") as f:
                return json.load(f)
        except Exception:
            return []

def save_json(file, data):
        try:
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Error saving file:", e)

def generate_id():
        # UUID4 generates a random unique id
        return str(uuid.uuid4())

def validate_phone(phone):
        # Accept phone numbers that start with +234 followed by 10 digits, or 0 followed by 10 digits
        if not isinstance(phone, str):
            return False
        phone = phone.strip()
        return re.match(r'^(\\+234|0)\\d{10}$', phone) is not None

def validate_nin(nin):
        # Nigerian NIN is 11 digits; validate as digits of length 11
        if not isinstance(nin, str):
            return False
        return re.match(r'^\\d{11}$', nin) is not None
