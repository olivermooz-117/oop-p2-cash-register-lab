#!/usr/bin/env python3

class CashRegister:
    """Cash Register class for tracking purchases, discounts, and transactions."""
    
    def __init__(self, discount=0):
        """
        Initialize cash register with optional discount.
        
        Args:
            discount (int): Percentage discount (0-100). Defaults to 0.
        """
        self.discount = discount
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
        if not isinstance(value, int):
            raise TypeError("Discount must be an integer")
        if not (0 <= value <= 100):
            raise ValueError("Discount must be between 0 and 100 inclusive")
        self._discount = value
    
    def add_item(self, item, price, quantity=1):
        """
        Add item(s) to the cash register.
        
        Args:
            item (str): Name of the item
            price (float): Price per unit
            quantity (int): Number of items (defaults to 1)
        """
        item_total = price * quantity
        self.total += item_total
        
        for _ in range(quantity):
            self.items.append(item)
        
        self.previous_transactions.append({
            'item': item,
            'price': price,
            'quantity': quantity,
            'item_total': item_total
        })
    
    def apply_discount(self):
        """
        Apply discount to total price.
        Prints success message with updated total or error message.
        """
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        """
        Remove the last transaction and update total and items.
        Returns total to 0.0 if all items have been removed.
        """
        if not self.previous_transactions:
            return
        
        last_transaction = self.previous_transactions.pop()
        quantity = last_transaction['quantity']
        
        for _ in range(quantity):
            if self.items:
                self.items.pop()
        
        self.total -= last_transaction['item_total']
        
        if self.total < 0:
            self.total = 0.0


# Test code (this won't run on CodeGrade, only when you run it manually)
if __name__ == "__main__":
    print("Running CashRegister tests...")
    
    # Test 1: Initialization
    register = CashRegister()
    assert register.total == 0, "Total should be 0"
    assert register.items == [], "Items should be empty list"
    print("✓ Initialization tests passed")
    
    # Test 2: Add items with optional quantity
    register.add_item("apple", 0.99)
    assert register.total == 0.99, "Total should be 0.99"
    assert register.items == ["apple"], "Items should contain apple"
    
    register.add_item("banana", 0.50, 3)
    assert register.total == 2.49, "Total should be 2.49"
    assert register.items == ["apple", "banana", "banana", "banana"], "Items should include multiples"
    print("✓ Add item tests passed")
    
    # Test 3: Apply discount
    register_with_discount = CashRegister(20)
    register_with_discount.add_item("book", 10.00)
    result = register_with_discount.apply_discount()
    assert result == "After the discount, the total price is $8.00.", "Discount message incorrect"
    assert register_with_discount.total == 8.00, "Total after discount should be 8.00"
    print("✓ Apply discount tests passed")
    
    # Test 4: Apply discount when none exists
    no_discount_register = CashRegister()
    no_discount_register.add_item("item", 5.00)
    result = no_discount_register.apply_discount()
    assert result == "There is no discount to apply.", "Error message incorrect"
    print("✓ No discount message test passed")
    
    # Test 5: Void last transaction
    test_register = CashRegister()
    test_register.add_item("item1", 10.00)
    test_register.add_item("item2", 5.00, 2)
    assert test_register.total == 20.00, "Total should be 20.00"
    
    test_register.void_last_transaction()
    assert test_register.total == 10.00, "Total after void should be 10.00"
    assert len(test_register.items) == 1, "Should have 1 item left"
    print("✓ Void transaction tests passed")
    
    print("\n✅ All tests passed!")