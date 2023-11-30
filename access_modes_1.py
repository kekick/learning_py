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

