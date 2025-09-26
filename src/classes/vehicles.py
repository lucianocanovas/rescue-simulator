class vehicle:
    def __init__(self, capacity):
        self.position = [None, None]
        self.capacity = capacity

    def move(self):
        pass

    def download(self):
        pass

    def findShortestPath(self):
        pass

class jeep(vehicle):
    def __init__(self):
        super().__init__(2)

class truck(vehicle):
    def __init__(self):
        super().__init__(3)

class car(vehicle):
    def __init__(self):
        super().__init__(1)

class motorcicle(vehicle):
    def __init__(self):
        super().__init__(1)

    def checkPerson():
        pass

    def kamikaze():
        pass