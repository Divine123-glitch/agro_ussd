from utils import load_json, save_json, gen_id, title_case, valid_phone, valid_nin
BUYERS_FILE = 'buyers.json'
FARMERS_FILE = 'farmers.json'

class Buyer:
    @staticmethod
    def register():
        print('\n--- Buyer Registration ---')
        while True:
            name = title_case(input('Enter full name: '))
            if name: break
            print('Name cannot be empty.')
        while True:
            nin = input('Enter NIN (11 digits): ').strip()
            if valid_nin(nin): break
            print('Invalid NIN. Must be 11 digits.')
        while True:
            phone = input('Enter phone (+234XXXXXXXXXX or 0XXXXXXXXXX): ').strip()
            if valid_phone(phone): break
            print('Invalid phone.')
        while True:
            password = input('Create password (min 4 chars): ').strip()
            if len(password) >= 4: break
            print('Password too short.')
        location = title_case(input('Enter location: '))
        buyer = {'id': gen_id(), 'name': name, 'nin': nin, 'phone': phone, 'password': password, 'location': location, 'requests': []}
        buyers = load_json(BUYERS_FILE)
        buyers.append(buyer)
        save_json(BUYERS_FILE, buyers)
        print('Buyer registered successfully. ID:', buyer['id'])

    @staticmethod
    def login():
        print('\n--- Buyer Login ---')
        buyers = load_json(BUYERS_FILE)
        while True:
            phone = input('Enter phone: ').strip()
            password = input('Enter password: ').strip()
            for b in buyers:
                if b['phone'] == phone and b['password'] == password:
                    print(f"Welcome {b['name']}!")
                    return b
            print('Invalid credentials. Try again.')

    @staticmethod
    def search_and_request(buyer):
        farmers = load_json(FARMERS_FILE)
        if not farmers:
            print('No farmers available.')
            return
        query = title_case(input('Enter product to search (partial or full name): ').strip())
        matches = []
        for f in farmers:
            for p in f.get('products', []):
                if query.lower() in p['product'].lower() and p.get('quantity', 0) > 0:
                    matches.append((f, p))
        if not matches:
            print('No matching products found.')
            return
        print('\nMatching listings:')
        for i, (f, p) in enumerate(matches, 1):
            print(f"{i}. Farmer: {f['name']} | Product: {p['product']} | Price: ₦{p['price']} | Qty: {p['quantity']} | Phone: {f['phone']}")
        while True:
            choice = input('Enter listing number to request (or blank to cancel): ').strip()
            if choice == '': return
            if not choice.isdigit():
                print('Enter a number or blank.')
                continue
            idx = int(choice)-1
            if not (0 <= idx < len(matches)):
                print('Invalid number.')
                continue
            f, p = matches[idx]
            while True:
                try:
                    qty = int(input(f"Enter quantity to request (available {p['quantity']}): ").strip())
                    break
                except ValueError:
                    print('Enter an integer quantity.')
            if qty <= 0:
                print('Quantity must be positive.')
                return
            if qty > p['quantity']:
                print('Requested quantity greater than available.')
                return
            # create request
            req = {'id': gen_id(), 'buyer_id': buyer['id'], 'buyer_name': buyer['name'], 'product': p['product'], 'quantity': qty}
            # add to farmer's requests
            farmers_all = load_json(FARMERS_FILE)
            for farmer_rec in farmers_all:
                if farmer_rec['id'] == f['id']:
                    farmer_rec.setdefault('requests', []).append(req)
            save_json(FARMERS_FILE, farmers_all)
            # add to buyer requests
            buyers_all = load_json(BUYERS_FILE)
            for buyer_rec in buyers_all:
                if buyer_rec['id'] == buyer['id']:
                    buyer_rec.setdefault('requests', []).append(req)
            save_json(BUYERS_FILE, buyers_all)
            print('Request sent to farmer.')
            return
