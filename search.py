from db import list_farmers
from utils import safe_input, pause

def search_by_product(previous_menu_callback=None):
    try:
        print("\n--- Search Farmers by Product ---")
        term = safe_input("Enter product name to search (partial allowed): ")
        if not term:
            raise ValueError("Search term cannot be empty")
        term = term.lower()

        farmers = list_farmers()
        results = [f for f in farmers if term in f.get("product", "").lower()]

        if not results:
            print("No farmers found for that product.")
            pause()
            return

        print(f"Found {len(results)} farmer(s):")
        for idx, f in enumerate(results, 1):
            try:
                print("=================================")
                print(f"\n{idx}. {f.get('name')} | Product: {f.get('product')} | Price: {f.get('price')}/{f.get('unit')} | Location: {f.get('location')} | Phone: {f.get('phone')}")
                print("=================================")
            except Exception:
                continue

        pause()
        return

    except Exception as e:
        print(f"Error during search: {e}")
        print("Returning to previous menu...")
        if previous_menu_callback:
            try:
                previous_menu_callback()
            except Exception:
                pass
        return
