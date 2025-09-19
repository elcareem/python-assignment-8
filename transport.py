"""
TASK: Create a Bus class.

Requirements:
1. Store bus capacity and passenger list.
2. Provide a method to add a passenger (if space available).
3. Provide a method to remove a passenger.
4. Provide a method to show all passengers.

Example Usage:
    metro_bus = Bus(capacity=3)
    metro_bus.add_passenger("John")
    metro_bus.add_passenger("Mary")
    metro_bus.add_passenger("Paul")
    metro_bus.add_passenger("Lisa")  # "Bus is full!"
    print(bus.show_passengers())  # ["John", "Mary", "Paul"]
"""

class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) >= self.capacity:
            print("Bus is full")
            return

        if passenger in self.passengers:
            print(f"{passenger} with name already in the bus")
        else:
            self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        if passenger not in self.passengers:
            print(f"{passenger} not in the bus")
        else:
            self.passengers.remove(passenger)

    def show_passengers(self):
        return self.passengers

metro_bus = Bus(capacity=3)
metro_bus.add_passenger("John")
metro_bus.add_passenger("Mary")
metro_bus.add_passenger("Paul")
metro_bus.remove_passenger("Pal")
metro_bus.add_passenger("Lisa")  
print(metro_bus.show_passengers())  








