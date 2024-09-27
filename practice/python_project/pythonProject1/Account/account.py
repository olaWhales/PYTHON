class Account:

    def __init__(self, first_name, last_name,  pin):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return 'success'

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            return self.check_balance()

