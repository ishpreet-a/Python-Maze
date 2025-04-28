class Coord2D:
    x, y = 0, 0
    def __init__(self, a, b):
        self.x = a
        self.y = b
    #
    def __eq__(self, o):
        return (self.x == o.x) and (self.y == o.y)
    #
    def __hash__(self):
        h = hash(self.x*self.y)
        #print('hash:', h)
        return h
    #
#
