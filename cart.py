"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""
class ShoppingCart:

    def __init__(self, shop_items):
        self.shop_items = shop_items
        self.cart_items = {}

    def add_item(self, item, quantity):
        if item in self.shop_items:
            if item in self.cart_items:
                self.cart_items.update({item: self.cart_items[item] + quantity})
            else:
                self.cart_items.update({item: quantity})            
        else:
            print("Item is not available")

    def remove_item(self, item, quantity):
        if item in self.cart_items:
            if 0 < quantity <= self.cart_items[item]:
                self.cart_items.update({item: self.cart_items[item] - quantity})
                if self.cart_items[item] == 0: 
                    self.cart_items.pop(item)
            else:
                print("Invalid quantity")
        else:
            print("Item is not available")


    def clear_cart(self):
        self.cart_items.clear()

    def calculate_total(self):  
        total = 0
        for cart_item, quantity in self.cart_items.items():
            for shop_item, price in self.shop_items.items():
                if cart_item == shop_item:
                    total += quantity * price

        return total



prices = {"Shirt": 5000, "Shoes": 12000}
cart = ShoppingCart(prices)
cart.add_item("Shirt", 2)
cart.add_item("Shirt", 3)
cart.add_item("Shoes", 3)


print(cart.calculate_total())  
cart.clear_cart()
print(cart.calculate_total())



