class CashRegister:
    """
    A cash register that can add items, apply discounts, and void last transactions.
    """
    
    def __init__(self, discount=None):
        """
        Initialize the cash register.
        
        Args:
            discount: Percentage discount off total (0-100 inclusive)
                     If no input, initializes as 0
        """
        # Allow for user input if discount is None
        if discount is None:
            try:
                user_input = input("Enter discount percentage (0-100): ")
                if user_input == "":
                    self._discount = 0
                else:
                    discount_value = int(user_input)
                    self.discount = discount_value  # Use property setter for validation
            except ValueError:
                print("Not valid discount")
                self._discount = 0
        else:
            self.discount = discount  # Use property setter for validation
        
        # Initialize other attributes
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the discount value."""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """
        Set discount with validation.
        Ensures discount is an integer between 0-100 inclusive.
        """
        # Ensure discount is an integer
        if not isinstance(value, int):
            try:
                value = int(value)
            except (ValueError, TypeError):
                print("Not valid discount")
                self._discount = 0
                return
        
        # Ensure discount is between 0-100 inclusive
        if 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0
    
    def add_item(self, item, price, quantity):
        """
        Add item(s) to the cash register.
        
        Args:
            item: Name of the item
            price: Price per unit
            quantity: Number of items being purchased
        """
        # Calculate total cost for this transaction
        item_total = price * quantity
        
        # Add to total
        self.total += item_total
        
        # Add item to items array (quantity times)
        for _ in range(quantity):
            self.items.append(item)
        
        # Add transaction record
        transaction = {
            'item': item,
            'price': price,
            'quantity': quantity,
            'item_total': item_total
        }
        self.previous_transactions.append(transaction)
        
        print(f"Added {quantity}x {item} @ ${price:.2f} each = ${item_total:.2f}")
    
    def apply_discount(self):
        """
        Apply discount as percentage off from total.
        """
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            discounted_total = self.total - discount_amount
            return f"After {self.discount}% discount, the total is ${discounted_total:.2f}."
        else:
            return f"No discount applied. Total is ${self.total:.2f}."
    
    def void_last_transaction(self):
        """
        Remove the last item of previous_transaction from array.
        Ensures price and items reflect correctly.
        """
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        
        # Get the last transaction
        last_transaction = self.previous_transactions.pop()
        
        # Remove items from items array
        item_name = last_transaction['item']
        quantity = last_transaction['quantity']
        
        # Remove the specified quantity of items from the end of items list
        removed_count = 0
        for _ in range(quantity):
            if self.items:
                # Remove from the end (most recent items)
                removed_item = self.items.pop()
                if removed_item == item_name:
                    removed_count += 1
        
        # Subtract from total
        self.total -= last_transaction['item_total']
        
        print(f"Voided {quantity}x {item_name}. Removed ${last_transaction['item_total']:.2f} from total.")
        if removed_count != quantity:
            print(f"Warning: Only found {removed_count} of {quantity} {item_name} to remove")
    
    def get_total(self):
        """Return the current total."""
        return self.total
    
    def get_items(self):
        """Return the list of items."""
        return self.items.copy()
    
    def get_previous_transactions(self):
        """Return the list of previous transactions."""
        return self.previous_transactions.copy()
    
    def show_receipt(self):
        """Display the current receipt."""
        print("\n" + "="*50)
        print("CASH REGISTER RECEIPT")
        print("="*50)
        
        if not self.previous_transactions:
            print("No items purchased yet.")
        else:
            # Display each transaction
            for i, transaction in enumerate(self.previous_transactions, 1):
                print(f"{i}. {transaction['quantity']}x {transaction['item']} @ ${transaction['price']:.2f} = ${transaction['item_total']:.2f}")
        
        print("-"*50)
        print(f"SUBTOTAL: ${self.total:.2f}")
        
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            print(f"DISCOUNT ({self.discount}%): -${discount_amount:.2f}")
            print(f"TOTAL DUE: ${self.total - discount_amount:.2f}")
        else:
            print(f"TOTAL DUE: ${self.total:.2f}")
        print("="*50)


# Example usage and testing
if __name__ == "__main__":
    print("="*50)
    print("CASH REGISTER SYSTEM")
    print("="*50)
    
    # Create cash register - this will prompt for user input
    print("\n--- Initializing Cash Register ---")
    register = CashRegister()  # Will ask user for discount
    
    print(f"\nCash register initialized with {register.discount}% discount")
    
    # Interactive menu for testing
    while True:
        print("\n" + "-"*40)
        print("OPTIONS:")
        print("1. Add item")
        print("2. Apply discount")
        print("3. Void last transaction")
        print("4. Show receipt")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            item = input("Enter item name: ")
            try:
                price = float(input("Enter price: $"))
                quantity = int(input("Enter quantity: "))
                register.add_item(item, price, quantity)
            except ValueError:
                print("Invalid input. Please enter numbers for price and quantity.")
        
        elif choice == '2':
            print(register.apply_discount())
        
        elif choice == '3':
            register.void_last_transaction()
        
        elif choice == '4':
            register.show_receipt()
        
        elif choice == '5':
            print("\nThank you for using the Cash Register System!")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    # Additional test cases for discount validation
    print("\n" + "="*50)
    print("TESTING DISCOUNT VALIDATION")
    print("="*50)
    
    # Test with invalid discount (outside range)
    print("\nTest 1: Invalid discount (150)")
    test1 = CashRegister(150)
    print(f"Result: discount = {test1.discount}")
    
    # Test with non-integer discount
    print("\nTest 2: Invalid discount (string)")
    test2 = CashRegister("twenty")
    print(f"Result: discount = {test2.discount}")
    
    # Test with valid discount
    print("\nTest 3: Valid discount (25)")
    test3 = CashRegister(25)
    print(f"Result: discount = {test3.discount}")