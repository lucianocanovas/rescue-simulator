class Vehicle:
    def __init__(self, capacity):
        self.position = [None, None]
        self.capacity = capacity

    def move(self):
        pass

    def download(self):
        pass

    def find_path(self):
        pass

class Jeep(Vehicle):
    def __init__(self):
        super().__init__(2)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(3)

class Car(Vehicle):
    def __init__(self):
        super().__init__(1)

class Motorcicle(Vehicle):
    def __init__(self):
        super().__init__(1)

    def check_load(self):
        pass

    def kamikaze(self):
        pass