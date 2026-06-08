class CashRegister:
    def __init__(self, discount=0):
        # takes one optional argument, a discount, on initialization
        self.discount = discount
        # sets an instance variable total to zero on initialization
        self.total = 0
        # sets an instance variable items to empty list on initialization
        self.items = []
        self.previous_transactions = []
    
    def add_item(self, title, price, quantity=1):
        """
        accepts a title and a price and increases the total
        also accepts an optional quantity
        doesn't forget about the previous total
        """
        item_total = price * quantity
        self.total += item_total
        
        # returns an array containing all items that have been added, including multiples
        for _ in range(quantity):
            self.items.append(title)
        
        # Store transaction for void functionality
        self.previous_transactions.append({
            'title': title,
            'price': price,
            'quantity': quantity,
            'item_total': item_total
        })
    
    def apply_discount(self):
        """
        applies the discount to the total price
        prints success message with updated total
        prints a string error message that there is no discount to apply
        """
        if self.discount > 0:
            # applies the discount to the total price
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # prints success message with updated total
            return f"After the discount, the total price is ${self.total:.2f}."
        else:
            # prints a string error message that there is no discount to apply
            return "There is no discount to apply."
    
    def void_last_transaction(self):
        """
        subtracts the last item from the total
        returns the total to 0.0 if all items have been removed
        """
        if self.previous_transactions:
            # Get the last transaction
            last_transaction = self.previous_transactions.pop()
            
            # subtracts the last item from the total
            self.total -= last_transaction['item_total']
            
            # Remove items from the items list
            quantity = last_transaction['quantity']
            for _ in range(quantity):
                if self.items:
                    self.items.pop()
            
            # returns the total to 0.0 if all items have been removed
            if self.total < 0:
                self.total = 0.0
    
    def get_items(self):
        """
        returns an array containing all items that have been added
        returns an array containing all items that have been added, including multiples
        """
        return self.items