"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append({"deposit": amount})
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            self.transactions.append({"withdrawal": amount})
        else:
            "Insufficient Balance"
    
    def get_balance(self):
        return self.balance

account_1 = BankAccount("Alice", 1000)

account_1.deposit(500)
account_1.withdraw(200)
print(account_1.get_balance())


