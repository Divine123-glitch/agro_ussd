from farmer import Farmer
from buyer import Buyer

def main_menu():
    while True:
        print("\n=== Agro USSD Platform ===")
        print("1. Farmer Login/Register")
        print("2. Buyer Login/Register (required to search)")
        print("3. Exit")
        choice = input("Select option: ").strip()
        if choice == "1":
            Farmer.menu()
        elif choice == "2":
            Buyer.menu()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main_menu()
