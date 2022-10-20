class Matrix:
    def __init__(self, values, g, h,parent, lastMoved=None, movement=None):
        if movement is None:
            movement = []
        if lastMoved is None:
            lastMoved = []
        self.values = values
        self.g = g
        self.h = h
        self.f = g + h
        self.lastMoved = lastMoved
        self.movement = movement
        self.parent = parent

    def print(self):
        for line in self.values:
            print(" ".join(line))
