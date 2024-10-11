class Television:

    def __init__(self):
        self.channel = 100
        self.volume_level = 0
        self.is0n = False

    def is_on(self):
        return self.isOn

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def get_channel(self):
            return self.channel

    def set_channel(self, channel: int):
        if self.isOn:
            self.channel = channel
        elif not self.isOn:
            self.channel = 1

    def decrease_channel(self, decrease_channel:int):
        if self.isOn == True and self.channel >= decrease_channel :
            self.channel -= decrease_channel
        else:
            self.channel = 1

    def get_volume(self):
        return self.volume_level

    def set_volume_level(self, volume_level):
        self.volume_level = volume_level

    def increase_voloume(self, increase_volume):
        if self.isOn == True and self.volume_level <= 0 :
            self.volume_level += increase_volume
        else:
            self.volume_level = 0

    def decrease_volume(self, decrease_volume):
        if self.isOn and self.volume_level >= decrease_volume:
            self.volume_level -= decrease_volume
        else:
            self.volume_level = 0








