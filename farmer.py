import os
from utils import load_json, save_json, generate_id, validate_phone, validate_nin
FARMERS_FILE = "farmers.json"

class Farmer:
        @staticmethod
        def menu():
            while True:
                print("\n--- Farmer Menu ---")
                print("1. Register")
                print("2. Login")
                print("3. Back")
                choice = input("Choose option: ").strip()
                if choice == "1":
                    Farmer.register()
                elif choice == "2":
                    Farmer.login()
                elif choice == "3":
                    break
                else:
                    print("Invalid option")

        @staticmethod
        def register():
            try:
                farmers = load_json(FARMERS_FILE)
                name = input("Enter full name: ").strip()
                if not name:
                    print("Name required.")
                    return
                nin = input("Enter NIN (11 digits): ").strip()
                if not validate_nin(nin):
                    print("Invalid NIN. It must be 11 digits.")
                    return
                phone = input("Enter phone (+234XXXXXXXXXX or 0XXXXXXXXXX): ").strip()
                if not validate_phone(phone):
                    print("Invalid phone. Must start with +234 or 0 and contain 11 digits in local form.")
                    return
                # prevent duplicate phone for farmers
                for f in farmers:
                    if f.get("phone") == phone:
                        print("A farmer with this phone already exists.")
                        return
                password = input("Create password (min 4 chars): ").strip()
                if len(password) < 4:
                    print("Password too short.")
                    return
                location = input("Enter location (city / LGA): ").strip()
                farmer_id = generate_id()
                products = []
                print("Add products. Type 'done' as product name when finished.")
                while True:
                    item = input(" Product name (or 'done'): ").strip()
                    if item.lower() == "done":
                        break
                    unit = input("  Unit (e.g. kg, bag, head): ").strip()
                    price_raw = input("  Price per unit (numeric): ").strip()
                    try:
                        price = float(price_raw)
                    except Exception:
                        print("  Invalid price. Skipping this product.")
                        continue
                    products.append({"item": item, "unit": unit, "price": price})
                farmers.append({
                    "id": farmer_id,
                    "name": name,
                    "nin": nin,
                    "phone": phone,
                    "password": password,
                    "location": location,
                    "products": products
                })
                save_json(FARMERS_FILE, farmers)
                print("Farmer registered successfully! Your Farmer ID:", farmer_id)
            except Exception as e:
                print("Error during farmer registration:", e)

        @staticmethod
        def login():
            try:
                farmers = load_json(FARMERS_FILE)
                phone = input("Enter phone: ").strip()
                password = input("Enter password: ").strip()
                for farmer in farmers:
                    if farmer.get("phone") == phone and farmer.get("password") == password:
                        print(f"Welcome {farmer.get('name')}!")
                        Farmer.dashboard(farmer)
                        return
                print("Invalid login details!")
            except Exception as e:
                print("Login error:", e)

        @staticmethod
        def dashboard(farmer):
            try:
                while True:
                    print(f"\n--- Farmer Dashboard ({farmer.get('name')}) ---")
                    print("1. Add Product")
                    print("2. View Products")
                    print("3. Logout")
                    choice = input("Choose: ").strip()
                    if choice == "1":
                        item = input(" Enter product name: ").strip()
                        unit = input(" Enter unit: ").strip()
                        price_raw = input(" Enter price: ").strip()
                        try:
                            price = float(price_raw)
                        except Exception:
                            print(" Invalid price. Operation cancelled.")
                            continue
                        farmer.setdefault("products", []).append({"item": item, "unit": unit, "price": price})
                        farmers = load_json(FARMERS_FILE)
                        for f in farmers:
                            if f.get("id") == farmer.get("id"):
                                f["products"] = farmer["products"]
                        save_json(FARMERS_FILE, farmers)
                        print("Product added successfully!")
                    elif choice == "2":
                        print("Your Products:")
                        for p in farmer.get("products", []):
                            print(f" - {p.get('item')} ({p.get('unit')}) at {p.get('price')}")
                    elif choice == "3":
                        break
                    else:
                        print("Invalid option")
            except Exception as e:
                print("Error in dashboard:", e)
