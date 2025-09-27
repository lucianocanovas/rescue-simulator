class Board:
    def __init__(self, width=50, height=50):
        self.tile_size = 16
        self.width = width
        self.height = height
        self.matrix = [[0 for column in range(width)] for row in range(height)]
        self.sprite = pygame.image.load("../../assets/board/board.png")

    def draw(self, surface):
        pass
