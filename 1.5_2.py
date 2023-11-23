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
elements = [(Line, Rect, Ellipse)[r(0, 2)](1,2,3,4) for i in range(217)]
'''elements = []
for i in range(217):
    x = r(1, 3)
    match x:
        case 1:
            elements.append(Line(r(1, 1000), r(1, 1000), r(1, 1000), r(1, 1000)))
        case 2:
            elements.append(Rect(r(1, 1000), r(1, 1000), r(1, 1000), r(1, 1000)))
        case 3:
            elements.append(Ellipse(r(1, 1000), r(1, 1000), r(1, 1000), r(1, 1000)))
'''
for i in elements:
    if type(i) == Line:
        i.sp, i.ep = (0, 0), (0, 0)
