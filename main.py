from farmer import Farmer
from buyer import Buyer

def main_menu():
    while True:
        print("\n--- AGRO USSD PLATFORM ---")
        print("1. Register as Farmer")
        print("2. Login as Farmer")
        print("3. Register as Buyer")
        print("4. Login as Buyer")
        print("5. Exit")

        choice = input("Choose option: ").strip()
        if choice == "1":
            Farmer.register()
        elif choice == "2":
            Farmer.login()
        elif choice == "3":
            Buyer.register()
        elif choice == "4":
            buyer = Buyer.login()
            if buyer:
                while True:
                    print("\n--- BUYER MENU ---")
                    print("1. Search Farmers")
                    print("2. Logout")
                    ch = input("Choose option: ").strip()
                    if ch == "1":
                        Buyer.search_farmers()
                    elif ch == "2":
                        break
                    else:
                        print("❌ Invalid choice.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main_menu()
