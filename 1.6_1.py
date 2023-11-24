class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
        return cls.__instance






    def __init__(self, name):
        self.name = name



a = SingletonFive('a')
b = SingletonFive('b')
c = SingletonFive('c')
d = SingletonFive('d')
e = SingletonFive('e')
f = SingletonFive('f')

print(SingletonFive.objects)

print(f)
