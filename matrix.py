class Matrix:
    def __init__(self, values, g, h, lastMoved=None):
        if lastMoved is None:
            lastMoved = []
        self.values = values
        self.g = g
        self.h = h
        self.f = g + h
        self.lastMoved = lastMoved
