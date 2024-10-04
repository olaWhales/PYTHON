class Account:

    def __init__(self , name , balance , pin):
        self.name = name
        self.balance = 0
        self.pin = pin

        def set_deposit(self , amount ):
            if amount <= self.balance:
                self.balance = self.balance + amount


