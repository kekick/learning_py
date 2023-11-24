class SingletonFive:
    objects = {1: None, 2: None, 3: None, 4: None, 5: None}

    def __new__(cls, *args, **kwargs):
        s5 = cls.objects
        for i in range(1, 6):
            if not s5.get(i):
                s5[i] = super().__new__(cls)

        return s5[max(cls.objects.keys()) if s5[max(cls.objects.keys())] else None]

    def __init__(self, name):
        self.name = name



a = SingletonFive('a')
b = SingletonFive('b')
c = SingletonFive('c')
d = SingletonFive('d')
e = SingletonFive('e')
f = SingletonFive('f')
g = SingletonFive('G')
print(SingletonFive.objects)

print(f)
print(g)