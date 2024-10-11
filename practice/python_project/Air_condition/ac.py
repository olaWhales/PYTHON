class Ac:

    def __init__(self):
        self.switch : bool = False
        self.temperature = 16

    def operate(self):
        return self.switch

    def power_on(self):
        self.switch = True

    def power_off(self):
        self.switch = False

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temp: int):
        self.switch = True
        temp = 1
        self.temperature += temp
        if self.temperature > 30:
            self.temperature = 30

    def decrease_temoerature(self, temp: int):
        self.switch = True
        self.temperature -= temp
        if self.temperature < 16:
            self.temperature = 16



