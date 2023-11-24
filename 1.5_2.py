import random
from random import randint as r


class Line:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


random.seed(1)
elements = [(Line, Rect, Ellipse)[r(0, 2)](1, 2, 3, 4) for i in range(217)]

for i in elements:
    if type(i) == Line:
        i.sp, i.ep = (0, 0), (0, 0)
