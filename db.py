import json
import threading
from pathlib import Path

DB_FILE = Path("data.json")
LOCK = threading.Lock()

def _ensure_db():
    try:
        if not DB_FILE.exists():
            DB_FILE.write_text(json.dumps({"farmers": [], "buyers": []}, indent=2))
    except Exception:
        raise

def read_db():
    try:
        _ensure_db()
        with LOCK:
            with DB_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        return {"farmers": [], "buyers": []}

def write_db(data):
    try:
        _ensure_db()
        with LOCK:
            with DB_FILE.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        return True
    except Exception:
        return False

def add_farmer(farmer_dict):
    try:
        data = read_db()
        data.setdefault("farmers", []).append(farmer_dict)
        return write_db(data)
    except Exception:
        return False

def add_buyer(buyer_dict):
    try:
        data = read_db()
        data.setdefault("buyers", []).append(buyer_dict)
        return write_db(data)
    except Exception:
        return False

def list_farmers():
    try:
        data = read_db()
        return data.get("farmers", [])
    except Exception:
        return []

def list_buyers():
    try:
        data = read_db()
        return data.get("buyers", [])
    except Exception:
        return []
