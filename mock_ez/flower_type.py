class FlowerType(object):
    def __init__(self, color: str, height: int):
        self.color = color
        self.height = height

    def flower_type(self):
        if self.color == 'red':
            return 'rose'
        if self.color == 'pink':
            return 'lotus'
        if self.color == 'yellow':
            return 'daisy'
