class Matrix:
    def __init__(self, values, g, h, lastMoved=None, movement=None):
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
