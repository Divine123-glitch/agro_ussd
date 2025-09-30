from utils import load_json, save_json, validate_phone, validate_nin, title_case, generate_id
from user import User

BUYERS_FILE = "buyers.json"
FARMERS_FILE = "farmers.json"

class Buyer(User):
    def __init__(self, name, phone, password, nin, location):
        super().__init__(name, phone, password, nin, location)

    def save(self):
        buyers = load_json(BUYERS_FILE)
        buyers.append(self.__dict__)
        save_json(BUYERS_FILE, buyers)

    @staticmethod
    def register():
        while True:
            name = title_case(input("Enter full name: "))
            if name:
                break
            print("❌ Name cannot be empty.")

        while True:
            phone = input("Enter phone number (+234 or 0...): ").strip()
            if validate_phone(phone):
                break
            print("❌ Invalid phone format.")

        while True:
            nin = input("Enter NIN (11 digits): ").strip()
            if validate_nin(nin):
                break
            print("❌ Invalid NIN. Must be 11 digits.")

        while True:
            password = input("Enter password: ").strip()
            if password:
                break
            print("❌ Password cannot be empty.")

        location = title_case(input("Enter your location: "))
        buyer = Buyer(name, phone, password, nin, location)
        buyer.save()
        print("✅ Buyer registered successfully!")

    @staticmethod
    def login():
        buyers = load_json(BUYERS_FILE)
        while True:
            phone = input("Enter phone: ").strip()
            password = input("Enter password: ").strip()
            for buyer in buyers:
                if buyer["phone"] == phone and buyer["password"] == password:
                    print(f"✅ Welcome Buyer {buyer['name']}!")
                    return buyer
            print("❌ Invalid credentials. Try again.")

    @staticmethod
    def search_farmers():
        farmers = load_json(FARMERS_FILE)
        if not farmers:
            print("❌ No farmers available.")
            return
        query = title_case(input("Enter product to search: "))
        results = [f for f in farmers if any(p["product"] == query for p in f["products"])]
        if results:
            print("Farmers with your product:")
            for f in results:
                print(f"{f['name']} - {f['location']} - {f['phone']}")
                for p in f["products"]:
                    if p["product"] == query:
                        print(f"{p['product']} | {p['unit']} | ₦{p['price']}")
        else:
            print("❌ No farmers found for that product.")
