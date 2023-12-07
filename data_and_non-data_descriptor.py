# #
# #
# class FloatValue:
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if isinstance(value, float):
#             instance.__dict__[self.name] = value
#         else:
#             raise TypeError("Присваивать можно только вещественный тип данных.")
#
#
# class Cell:
#     value = FloatValue()
#
#     def __init__(self, value=0.0):
#         self.value = value
#
#
#
# class TableSheet:
#
#     def __init__(self, N, M):
#         self.cells = [[Cell() for _ in range(M)] for _ in range(N)]
#
#     def show(self):
#         for i in self.cells:
#             print('', end='\n')
#             for j in i:
#                 print(j.value, end=' ')
#
#     def add_line(self, x, y, cell):
#         self.cells[x][y] = cell
#


# counter = 1.0
# table = TableSheet(5, 3)
# for i in range(5):
#     for j in range(3):
#         table.add_line(i, j, Cell(counter))
#         counter += 1.0
#
# table.show()


"""_________________________________________________________________________________________________________________"""

#
# class ValidateString:
#
#     def __init__(self, minl, maxl):
#         self.min_length = minl
#         self.max_length = maxl
#
#     def validate(self, string):
#         return type(string) == str and self.min_length <= len(string) <= self.max_length
#
#
# class StringValue:
#
#     def __init__(self, validator):
#         self.validator = validator
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if self.validator.validate(value):
#             instance.__dict__[self.name] = value
#         else:
#             pass
#
#
# class RegisterForm:
#     login = StringValue(validator=ValidateString(9, 20))
#     password = StringValue(validator=ValidateString(9, 20))
#     email = StringValue(validator=ValidateString(9, 20))
#
#     def __init__(self, login, password, email):
#         self.login = login
#         self.password = password
#         self.email = email
#
#     def get_fields(self):
#         return [self.login, self.password, self.email]
#
#     def show(self):
#         print(f"<form>\nЛогин:{self.login}\nПароль:{self.password}\nEmail:{self.email}\n</form>")


"""_________________________________________________________________________________________________________________"""

#
# class SuperShop:
#
#     def __init__(self, name):
#         self.name = name
#         self.goods = []
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
#
# class StringValue:
#     def __init__(self, min, max):
#         self.value = ''
#         self.min = min
#         self.max = max
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if isinstance(value, str) and self.min <= len(value) <= self.max:
#             instance.__dict__[self.name] = value
#
#
# class PriceValue:
#
#     def __init__(self, max):
#         self.value = -1
#         self.max = max
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if isinstance(self.value, (int, float)) and 0 <= value <= self.max:
#             instance.__dict__[self.name] = value
#
#
# class Product:
#
#     name = StringValue(2, 50)
#     price = PriceValue(max=10000)
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# shop = SuperShop("У Балакирева")
# shop.add_product(Product("Курс по Python", 0))
# shop.add_product(Product("Курс по Python ООП", 2000))
# for p in shop.goods:
#     print(f"{p.name}: {p.price}")
# print(shop.name)
"""_________________________________________________________________________________________________________________"""

#
# class Bag:
#
#     def __init__(self, max_weight):
#         self.__things = []
#         self.max_weight = max_weight
#
#     @property
#     def things(self):
#         return self.__things
#
#     def add_thing(self, thing):
#         if self.get_total_weight() + thing.weight <= self.max_weight:
#             self.__things.append(thing)
#
#     def remove_thing(self, indx):
#         del self.__things[indx]
#
#     def get_total_weight(self):
#         return sum(thing.weight for thing in self.things)
#
#
# class Thing:
#
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
"""_________________________________________________________________________________________________________________"""


class IntValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__[self.name] = value
        else:
            instance.__dict__[self.name] = 0


class Telecast:
    id = IntValue()
    duration = IntValue()

    def __init__(self, id, name, dur):
        self.id = id
        self.duration = dur
        self.__name = name if isinstance(name, str) else ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other_name):
        self.__name = other_name


class TVProgram:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        if isinstance(tl, Telecast):
            self.items.append(tl)

    def remove_telecast(self, indx):
        item = None
        for i in self.items:
            if i.id == indx:
                item = i
                break
        if item in self.items:
            self.items.remove(item)


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast('jani', "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
pr.remove_telecast(1)

