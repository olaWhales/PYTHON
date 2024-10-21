class Burger:

    def __init__(self, name: str):
        self.name = name
        self.type = type #turn this to none
        self.price = 0
        self.size = "MIDIUM"
        # self.size = "BIG"  #it cancelled this

    def set_name(self, name):
        self.name = name

    def set_type(self, types):
        self.type = types

    def set_price(self, price):
        self.price = price

    def set_size(self, size):
        self.size = size

    def get_base_price(self):#it added
        return self.price   #only return price

    def set_base_price(self, size): #it included else statement
        if size == "BIG":
            self.price = 500 * 1.5

    def set_adjusted_price(self, size):
        if size == "MIDIUM":
            self.price = 500 * 1.2

    def get_Adjusted_price(self):
        return self.price


