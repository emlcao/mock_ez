class FlowerType(object):
    def __init__(self, color, height):
        self.color = color
        self.height = height

    def flower_type(self):
        if self.color == 'red':
            return 'rose'
        if self.color == 'blue':
            return 'lotus'
        if self.color == 'yellow':
            return 'daisy'
