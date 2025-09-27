class Item :
    def __init__(self, value : int, position : tuple[int, int], image_path : str):
        self.value = value
        self.position = position
        self.sprite = image_path
        
class Person (Item):
    def __init__(self, position, image_path):
        super().__init__(50, position, image_path)

class Supply (Item):
    def __init__(self, value, position, sup_type : str, image_path ):
        super().__init__(value, position, image_path)
        self.sup_type = sup_type
