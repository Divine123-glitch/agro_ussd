from utils import load_json, save_json, validate_phone, validate_nin, title_case, generate_id
from user import User

FARMERS_FILE = "farmers.json"

class Farmer(User):
    def __init__(self, name, phone, password, nin, location):
        super().__init__(name, phone, password, nin, location)
        self.products = []

    def add_products(self):
        while True:
            product = title_case(input("Enter product name: "))
            unit = title_case(input("Enter unit (e.g., kg, bag): "))
            while True:
                try:
                    price = float(input("Enter price: "))
                    break
                except ValueError:
                    print("❌ Invalid price. Enter a number.")
            self.products.append({"product": product, "unit": unit, "price": price})
            more = input("Add another product? (y/n): ").lower()
            if more != "y":
                break

    def save(self):
        farmers = load_json(FARMERS_FILE)
        farmers.append(self.__dict__)
        save_json(FARMERS_FILE, farmers)

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
        farmer = Farmer(name, phone, password, nin, location)
        farmer.add_products()
        farmer.save()
        print("✅ Farmer registered successfully!")

    @staticmethod
    def login():
        farmers = load_json(FARMERS_FILE)
        while True:
            phone = input("Enter phone: ").strip()
            password = input("Enter password: ").strip()
            for farmer in farmers:
                if farmer["phone"] == phone and farmer["password"] == password:
                    print(f"✅ Welcome Farmer {farmer['name']}!")
                    return farmer
            print("❌ Invalid credentials. Try again.")
