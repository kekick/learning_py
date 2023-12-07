class CLock:

    def __init__(self, time=0):
        if self.__check_time(time):
            self.__time = time
        else:
            raise ValueError("Incorrect data type")

    def __check_time(self, tm):
        if type(tm) == int and 0 <= tm < 100000:
            return True

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


class Money:

    def __init__(self, money):
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def add_money(self, extra_money):
        if self.__check_money(extra_money.__money):
            self.__money += extra_money.__money

    def get_money(self):
        return self.__money

    def __check_money(self, money):
        if isinstance(money, int) and money >= 0:
            return True


class Book:

    def __init__(self, auth, book_name, price):
        if self.__chek_pt(auth):
            self.__author = auth
        if self.__chek_pt(book_name):
            self.__title = book_name
        if self.__chek_pt(price, type='price'):
            self.__price = price

    def __chek_pt(self, param, type="auth"):
        if type == "auth":
            if isinstance(param, str):
                return True
        elif type == "price":
            if isinstance(param, int) and param > -1:
                return True

    def set_title(self, title):
        if self.__chek_pt(title):
            self.__title = title

    def set_author(self, auth):
        if self.__chek_pt(auth):
            self.__author = auth

    def set_price(self, price):
        if self.__chek_pt(price, type="price"):
            self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


class Line:

    def __init__(self, x1, y1, x2, y2):
        self.__x1, self.__x2 = x1, x2
        self.__y1, self.__y2 = y1, y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1, self.__x2 = x1, x2
        self.__y1, self.__y2 = y1, y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())


class Point:

    def __init__(self, x, y):
        self.__x, self.__y = x, y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:

    def __init__(self, *args):
        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]
        elif len(args) == 4 and all(map(lambda x: isinstance(x, int), args)):
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        else:
            pass

    def set_coords(self, sp, ep):
        if isinstance(sp, Point) and isinstance(ep, Point):
            self.__ep = ep
            self.__sp = sp

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        x1y1 = self.get_coords()[0].get_coords()
        x2y2 = self.get_coords()[1].get_coords()
        print(f"Прямоугольник с координатами: {x1y1} {x2y2}")






