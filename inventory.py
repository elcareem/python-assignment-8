"""
TASK: Create an Inventory class.

Requirements:
1. Store items in a dictionary (item_name → quantity).
2. Provide a method to add items (with quantity).
3. Provide a method to remove items (only if available).
4. Provide a method to update stock levels.
5. Provide a method to display all inventory items.

Example Usage:
    treasure_store = Inventory()
    favour_store = Inventory()

    treasure_store.add_item("Apples", 50)
    treasure_store.add_item("Bananas", 30)
    treasure_store.remove_item("Apples", 10)
    print(treasure_store.show_inventory())  # {"Apples": 40, "Bananas": 30}

    favour_store.add_item("Milk", 50)
    favour_store.add_item("Garri", 30)
    favour_store.remove_item("Milk", 40)
    print(treasure_store.show_inventory())  # {"Milk": 10, "Garri": 30}
"""
class Inventory:
    def __init__(self):
        self.store = {}

    def add_item(self, item, quantity):
        if item not in self.store:
            if quantity > 0:
                self.store.update({item: quantity})
            else:
                return "Invalid quantity"

    def remove_item(self, item, quantity):
        if item not in self.store:
            return "Item not available"
        if 0 < quantity <= self.store[item]: 
            self.store.update({item: self.store[item] - quantity})        
            if self.store[item] == 0:
                self.store.pop(item)
        else:
            return "Invalid quantity"
    
    def update_stock(self, item, quantity):
        if item in self.store:
            if quantity > 0:
                self.store.update({item: self.store[item] + quantity})
            else:
                return "Invalid quantity"


    def show_inventory(self):
        return self.store


treasure_store = Inventory()
favour_store = Inventory()

treasure_store.add_item("Apples", 50)
treasure_store.add_item("Bananas", 30)
print(treasure_store.remove_item("Apples", 50))
print(treasure_store.show_inventory())  

favour_store.add_item("Milk", 50)
favour_store.add_item("Garri", 30)
favour_store.remove_item("Milk", 40)
print(favour_store.show_inventory())  
