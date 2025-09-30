from utils import load_json, save_json, gen_id, title_case, valid_phone, valid_nin
FARMERS_FILE = 'farmers.json'

class Farmer:
    @staticmethod
    def register():
        print('\n--- Farmer Registration ---')
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
        location = title_case(input('Enter location (city/LGA): '))
        farmer = {
            'id': gen_id(),
            'name': name,
            'nin': nin,
            'phone': phone,
            'password': password,
            'location': location,
            'products': [],
            'requests': []
        }
        print('Add products (type DONE as product name when finished).')
        while True:
            prod = input(' Product name (or DONE): ').strip()
            if prod.upper() == 'DONE': break
            prod = title_case(prod)
            unit = input('  Unit (e.g. kg, bag): ').strip()
            while True:
                try:
                    price = float(input('  Price per unit: ').strip())
                    break
                except ValueError:
                    print('  Invalid price. Enter a number.')
            while True:
                try:
                    qty = int(input('  Available quantity (integer): ').strip())
                    break
                except ValueError:
                    print('  Invalid quantity. Enter an integer.')
            farmer['products'].append({'product': prod, 'unit': unit, 'price': price, 'quantity': qty})
        farmers = load_json(FARMERS_FILE)
        farmers.append(farmer)
        save_json(FARMERS_FILE, farmers)
        print('Farmer registered successfully. Your ID:', farmer['id'])

    @staticmethod
    def login():
        print('\n--- Farmer Login ---')
        farmers = load_json(FARMERS_FILE)
        while True:
            phone = input('Enter phone: ').strip()
            password = input('Enter password: ').strip()
            for f in farmers:
                if f['phone'] == phone and f['password'] == password:
                    print(f"Welcome {f['name']}!")
                    return f
            print('Invalid credentials. Try again.')

    @staticmethod
    def update_details(farmer):
        farmers = load_json(FARMERS_FILE)
        for f in farmers:
            if f['id'] == farmer['id']:
                new_name = input(f"Enter new name (leave blank to keep '{f['name']}'): ").strip()
                if new_name:
                    f['name'] = title_case(new_name)
                new_loc = input(f"Enter new location (leave blank to keep '{f['location']}'): ").strip()
                if new_loc:
                    f['location'] = title_case(new_loc)
                new_pass = input('Enter new password (leave blank to keep current): ').strip()
                if new_pass:
                    f['password'] = new_pass
                save_json(FARMERS_FILE, farmers)
                print('Details updated.')
                return
        print('Farmer not found.')

    @staticmethod
    def add_product(farmer):
        farmers = load_json(FARMERS_FILE)
        for f in farmers:
            if f['id'] == farmer['id']:
                prod = title_case(input('Enter product name: ').strip())
                unit = input('Enter unit: ').strip()
                while True:
                    try:
                        price = float(input('Enter price: ').strip())
                        break
                    except ValueError:
                        print('Invalid price.')
                while True:
                    try:
                        qty = int(input('Enter available quantity: ').strip())
                        break
                    except ValueError:
                        print('Invalid quantity.')
                f['products'].append({'product': prod, 'unit': unit, 'price': price, 'quantity': qty})
                save_json(FARMERS_FILE, farmers)
                print('Product added.')
                return
        print('Farmer not found.')

    @staticmethod
    def view_requests(farmer):
        farmers = load_json(FARMERS_FILE)
        for f in farmers:
            if f['id'] == farmer['id']:
                reqs = f.get('requests', [])
                if not reqs:
                    print('No requests at the moment.')
                    return
                print('\nBuyer requests:')
                for i, r in enumerate(reqs, 1):
                    print(f"{i}. Buyer: {r['buyer_name']} | Product: {r['product']} | Qty: {r['quantity']}")
                while True:
                    choice = input('Enter request number to accept (or press Enter to go back): ').strip()
                    if choice == '': return
                    if not choice.isdigit():
                        print('Enter a number or blank.')
                        continue
                    idx = int(choice)-1
                    if not (0 <= idx < len(reqs)):
                        print('Invalid number.')
                        continue
                    req = reqs.pop(idx)
                    # find product and deduct
                    for p in f['products']:
                        if p['product'] == req['product']:
                            if p['quantity'] >= req['quantity']:
                                p['quantity'] -= req['quantity']
                                print(f"Accepted. Deducted {req['quantity']} from {p['product']}. New qty: {p['quantity']}")
                            else:
                                print('Insufficient quantity; cannot accept.')
                                f.setdefault('requests', []).append(req)
                            break
                    save_json(FARMERS_FILE, farmers)
                    return
        print('Farmer not found.')
