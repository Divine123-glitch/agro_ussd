import json, os, uuid, re

def load_json(filename):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def gen_id():
    import uuid
    return str(uuid.uuid4())

def title_case(s):
    try:
        return s.strip().title()
    except Exception:
        return s

def valid_phone(phone):
    import re
    if not isinstance(phone, str):
        return False
    phone = phone.strip()
    if re.fullmatch(r'\+234\d{10}', phone):
        return True
    if re.fullmatch(r'0\d{10}', phone):
        return True
    return False

def valid_nin(nin):
    return isinstance(nin, str) and nin.isdigit() and len(nin) == 11
