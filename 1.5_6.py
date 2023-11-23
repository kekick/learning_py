class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{obj.name}: {obj.price}" for obj in self.goods]


class Table:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:

    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
tv1 = TV('SAMSUNG', 13000)
tv2 = TV("LG", 9000)
tab1 = Table('Wooden', 5000)
nb1 = Notebook('Samsung',14000)
nb2 = Notebook("ASUS", 20000)
cup1 = Cup('Pint', 300)
for i in [tv1, tv2, tab1, nb1, nb2, cup1]:
    cart.add(i)

print(cart.get_list())