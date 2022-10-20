class Matrix:
    def __init__(self, values, g, h):
        self.values = values
        self.g = g
        self.h = h
        self.f = g + h
