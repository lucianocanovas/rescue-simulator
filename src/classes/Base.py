class Base :
    def __init__(self, position : tuple[int, int], radius : int = 0, vehicles : [] = None):
        self.position = position
        self.radius = radius
        self.vehicles = vehicles if vehicles is not None else []

