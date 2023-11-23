class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c

        for lenth in self.__dict__.values():
            if not isinstance(lenth, (int, float)) or lenth <= 0:
                return 1
        if a + b <= c or a + c <= b or c + b <= a:
            return 2

        else:
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, 2.3, 'qwf')
print(tr.is_triangle())