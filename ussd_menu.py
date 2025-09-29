from utils import safe_input

def main_menu():
    print("\n--- AGRO USSD ---")
    print("1. Register as Farmer")
    print("2. Register as Buyer")
    print("3. Search Farmers by Product")
    print("4. Exit")
    choice = safe_input("Select option: ")
    return choice
