from farmer import Farmer
from buyer import Buyer

def main_menu():
    while True:
        print('\n=== AGRO USSD (CLI) ===')
        print('1. Farmer: Register')
        print('2. Farmer: Login')
        print('3. Buyer: Register')
        print('4. Buyer: Login')
        print('5. Exit')
        choice = input('Choose option: ').strip()
        if choice == '1':
            Farmer.register()
        elif choice == '2':
            farmer = Farmer.login()
            if farmer:
                while True:
                    print('\n--- Farmer Menu ---')
                    print('1. Update Details')
                    print('2. Add Product')
                    print('3. View Requests')
                    print('4. Logout')
                    ch = input('Choose: ').strip()
                    if ch == '1':
                        Farmer.update_details(farmer)
                    elif ch == '2':
                        Farmer.add_product(farmer)
                    elif ch == '3':
                        Farmer.view_requests(farmer)
                    elif ch == '4':
                        break
                    else:
                        print('Invalid choice.')
        elif choice == '3':
            Buyer.register()
        elif choice == '4':
            buyer = Buyer.login()
            if buyer:
                while True:
                    print('\n--- Buyer Menu ---')
                    print('1. Search and Request')
                    print('2. Logout')
                    ch = input('Choose: ').strip()
                    if ch == '1':
                        Buyer.search_and_request(buyer)
                    elif ch == '2':
                        break
                    else:
                        print('Invalid choice.')
        elif choice == '5':
            print('Goodbye.')
            break
        else:
            print('Invalid option.')

if __name__ == "__main__":
    main_menu()
