"""
TASK: Create a RestaurantOrder class.

Requirements:
1. Store orders in a dictionary (item → quantity).
2. Provide a method to add items to the order.
3. Provide a method to remove items from the order.
4. Provide a method to calculate the total bill (use a price list dictionary).
5. Provide a method to show the current order.

Example Usage:
    prices = {"Pizza": 2000, "Burger": 1500, "Drink": 500}
    order = RestaurantOrder(prices)
    order.add_item("Pizza", 2)
    order.add_item("Drink", 3)
    print(order.calculate_total())  # 5500
"""

class RestaurantOrder:
    def __init__(self, menu):
        self.menu = menu
        self.orders = {}

    def add_item(self, item, quantity):
        if item in self.menu:
            if quantity > 0:
                if item in self.orders:
                    self.orders.update({item: self.orders[item] + quantity})
                else:
                    self.orders.update({item: quantity})
            else:
                print("Invalid quantity")
        else:
            print(f"{item} not available on menu")
    

    def remove_item(self, item, quantity):
        if item in self.orders:
            if 0 < quantity <= self.orders[item]:
                self.orders.update({item: self.orders[item] - quantity})
                if self.orders[item] == 0:
                    self.orders.pop(item)
            else:
                print("Invalid quantity")
        else:
            print(f"{item} not in order")

    
    def calculate_total(self):
        total = 0
    
        for order_item in self.orders:
            for item, price in self.menu.items():
                if order_item == item:
                    total += self.orders[order_item] * price

        return total
            


prices = {"Pizza": 2000, "Burger": 1500, "Drink": 500}
order = RestaurantOrder(prices)
order.add_item("Pizza", 2)
order.add_item("Pizza", 2)
order.add_item("Burger", 3)
order.remove_item("Pizza", 2)

print(order.menu)
print(order.orders)

print(order.calculate_total())

