from utils import load_json, save_json, generate_id, validate_phone, validate_nin
BUYERS_FILE = "buyers.json"
FARMERS_FILE = "farmers.json"

class Buyer:
        @staticmethod
        def menu():
            while True:
                print("\n--- Buyer Menu ---")
                print("1. Register")
                print("2. Login (required to search)")
                print("3. Back")
                choice = input("Choose option: ").strip()
                if choice == "1":
                    Buyer.register()
                elif choice == "2":
                    Buyer.login()
                elif choice == "3":
                    break
                else:
                    print("Invalid option")

        @staticmethod
        def register():
            try:
                buyers = load_json(BUYERS_FILE)
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
                # prevent duplicate phone for buyers
                for b in buyers:
                    if b.get("phone") == phone:
                        print("A buyer with this phone already exists.")
                        return
                password = input("Create password (min 4 chars): ").strip()
                if len(password) < 4:
                    print("Password too short.")
                    return
                buyer_id = generate_id()
                buyers.append({"id": buyer_id, "name": name, "nin": nin, "phone": phone, "password": password})
                save_json(BUYERS_FILE, buyers)
                print("Buyer registered successfully! Your Buyer ID:", buyer_id)
            except Exception as e:
                print("Error during buyer registration:", e)

        @staticmethod
        def login():
            try:
                buyers = load_json(BUYERS_FILE)
                phone = input("Enter phone: ").strip()
                password = input("Enter password: ").strip()
                for buyer in buyers:
                    if buyer.get("phone") == phone and buyer.get("password") == password:
                        print(f"Welcome {buyer.get('name')}!")
                        Buyer.dashboard(buyer)
                        return
                print("Invalid login details!")
            except Exception as e:
                print("Login error:", e)

        @staticmethod
        def dashboard(buyer):
            try:
                while True:
                    print("\n--- Buyer Dashboard ---")
                    print("1. Search Farmers by Product")
                    print("2. Logout")
                    choice = input("Choose: ").strip()
                    if choice == "1":
                        Buyer.search_farmers()
                    elif choice == "2":
                        break
                    else:
                        print("Invalid option")
            except Exception as e:
                print("Error in buyer dashboard:", e)

        @staticmethod
        def search_farmers():
            try:
                farmers = load_json(FARMERS_FILE)
                query = input("Enter product to search (partial allowed): ").strip().lower()
                if not query:
                    print("Empty search term.")
                    return
                results = []
                for farmer in farmers:
                    for p in farmer.get("products", []):
                        try:
                            if query in p.get("item", "").lower():
                                results.append({
                                    "farmer_name": farmer.get("name"),
                                    "location": farmer.get("location"),
                                    "phone": farmer.get("phone"),
                                    "product": p
                                })
                        except Exception:
                            continue
                if not results:
                    print("No farmers found for that product.")
                    return
                print(f"Found {len(results)} matching product(s):")
                for idx, r in enumerate(results, 1):
                    prod = r.get("product", {})
                    print(f"\n{idx}. Farmer: {r.get('farmer_name')} | Product: {prod.get('item')} | Price: {prod.get('price')}/{prod.get('unit')} | Location: {r.get('location')} | Phone: {r.get('phone')}")
            except Exception as e:
                print("Error during search:", e)
