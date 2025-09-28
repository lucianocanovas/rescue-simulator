class Mine:
    def __init__(self, x, y, radius_x, radius_y):
        self.position = [x, y]
        self.radiusX = radius_x
        self.radiusY = radius_y

class MineG2(Mine):
    def __init__(self, x, y):
        super().__init__(x, y, 7, 7)

    def teleport(self):
        pass