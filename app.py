import sys

class GhislaineHutApp:
    def __init__(self):
        self.restaurant_name = "Ghislaine Hut"
        self.tax_rate = 0.25
        # Pre-populated menu for immediate usability
        self.menu = {
            1: {"name": "Signature Smash Burger", "price": 14.50},
            2: {"name": "Spicy Fried Chicken", "price": 12.00},
            3: {"name": "Truffle Parmesan Fries", "price": 8.50},
            4: {"name": "Woodfire Margherita", "price": 18.00},
            5: {"name": "Artisan Lemonade", "price": 4.50}
        }
        # Stores cart items as {item_id: quantity}
        self.cart = {}

    def display_menu(self):
        print(f"\n--- {self.restaurant_name} Menu ---")
        print(f"{'ID':<4} | {'Item':<25} | {'Price':<10}")
        print("-" * 45)
        for key, item in self.menu.items():
            print(f"[{key}]  | {item['name']:<25} | ${item['price']:.2f}")
        print("-" * 45)

    def add_item(self):
        self.display_menu()
        try:
            choice = int(input("\nEnter the ID of the item to add: "))
            if choice not in self.menu:
                print("Invalid item ID. Please try again.")
                return

            qty = int(input(f"Enter quantity for {self.menu[choice]['name']}: "))
            if qty <= 0:
                print("Quantity must be 1 or greater.")
                return

            if choice in self.cart:
                self.cart[choice] += qty
            else:
                self.cart[choice] = qty
            
            print(f"Success: Added {qty}x {self.menu[choice]['name']} to your cart.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values only.")

    def view_cart(self):
        if not self.cart:
            print("\nYour cart is currently empty.")
            return False

        print("\n--- Current Cart ---")
        subtotal = 0.0
        for key, qty in self.cart.items():
            item = self.menu[key]
            line_total = item['price'] * qty
            subtotal += line_total
            print(f"{qty}x {item['name']:<25} ${line_total:.2f}")
        
        print("-" * 35)
        print(f"Current Subtotal: {'':<9} ${subtotal:.2f}")
        return True

    def checkout(self):
        if not self.view_cart():
            print("Action Denied: Add items to your cart before checking out.")
            return

        # Calculate financials
        subtotal = sum(self.menu[k]['price'] * v for k, v in self.cart.items())
        tax = subtotal * self.tax_rate
        total = subtotal + tax

        # Print final receipt
        print("\n" + "="*45)
        print(f"         {self.restaurant_name.upper()} - FINAL RECEIPT")
        print("="*45)
        for key, qty in self.cart.items():
            item = self.menu[key]
            print(f"{qty}x {item['name']:<25} ${item['price'] * qty:.2f}")
        print("-" * 45)
        print(f"Subtotal: {'':<21} ${subtotal:.2f}")
        print(f"Tax (25%): {'':<20} ${tax:.2f}")
        print("="*45)
        print(f"TOTAL DUE: {'':<20} ${total:.2f}")
        print("="*45)
        print("Order confirmed. Thank you for your business!\n")
        sys.exit(0)

    def run(self):
        print(f"=== Welcome to {self.restaurant_name} ===")
        print("Online Ordering Terminal")
        
        while True:
            print("\nMain Menu:")
            print("[1] View Menu & Add Item")
            print("[2] View Cart")
            print("[3] Checkout & Pay")
            print("[4] Exit Terminal")
            
            choice = input("\nSelect an operation (1-4): ")

            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.view_cart()
            elif choice == '3':
                self.checkout()
            elif choice == '4':
                print("Session terminated. Goodbye.")
                sys.exit(0)
            else:
                print("Error: Invalid command. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    app = GhislaineHutApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user. Exiting safely.")
        sys.exit(0)
