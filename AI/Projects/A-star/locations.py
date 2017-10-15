from math import sqrt

class Location():
    node = None
    pos = None
    cons = None
    def __init__(self, node, pos, cons):
        self.node = node
        self.pos = pos
        self.cons = cons

    def set_cons(c):
        self.cons = c

    def calc_distance(p1, p2):
        return sqrt( (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 )
