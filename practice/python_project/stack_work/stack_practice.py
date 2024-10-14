class Stack:

    def __init__(self, capacity: int):
        self.capacity = 0
        self.size = [self.capacity]
        self.element = 0


    def is_empty(self):
        var = self.size == 0
        return True

    def push(self , element: int):
        if element < self.capacity:
            self.size += [element]


    def pop(self):
        if self.element < self.capacity:
            self.size = self.capacity -1
            self.size -= [self.element]

    def get_state(self):
        return self.size

    def is_full(self) -> bool:
        return self.size == self.capacity




