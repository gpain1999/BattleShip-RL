class Boat:
    def __init__(self, name, size, position, orientation):
        self.name = name
        self.size = size
        self.position = position
        self.orientation = orientation

    def is_hit(self, row, col):
        if self.orientation == 'horizontal':
            if row != self.position[0]:
                return False
            if col < self.position[1] or col > self.position[1] + self.size - 1:
                return False
            return True
        else:
            if col != self.position[1]:
                return False
            if row < self.position[0] or row > self.position[0] + self.size - 1:
                return False
            return True