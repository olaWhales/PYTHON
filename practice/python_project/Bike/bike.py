
class Auto_bike:

    def __init__(self):
        self.turned_on : bool = False
        self.gear_speed = 0
        self.speed = 0
        self.gear = 0


    def turn_on(self):
        self.turned_on = True

    def turn_off(self):
        self.turned_on = False

    def switch(self):
            return self.turned_on

    def acceleration_on_1(self,gear_speed, speed):
        self.turned_on = True
        if gear_speed == 1:
            if 0 < speed <= 20:
                self.speed = speed + 1

                if speed > 20:
                    self.gear_speed = 2
                return self.speed

    def acceleration_on_2(self,gear_speed, speed):
        self.turned_on = True
        if gear_speed == 2:
            if 20 < speed <= 30:
                self.speed = speed + 2

                if speed > 30:
                    self.gear_speed = 2
                return self.speed

    def acceleration_on_3(self, gear_speed, speed):
        self.turned_on = True
        if gear_speed == 3:
            if 30 < speed <= 40:
                self.speed = speed + 3

                if speed > 40:
                    self.gear_speed = 3
                return self.speed

    def acceleration_on_4(self, gear_speed , speed):
        self.turned_on = True
        if gear_speed == 4:
            if 40 < speed <= 100:
                self.speed = speed + 4

                if speed > 50:
                    self.gear_speed = 4
                return self.speed








