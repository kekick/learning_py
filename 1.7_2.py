from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper()

    @staticmethod
    def check_card_number(number):
        if type(number) != str:
            return False
        number_lst = number.split("-")
        for id, num in enumerate(number_lst):
            if not all(map(lambda x: x.isdigit(), (_ for _ in num))) or len(num) != 4 or id == 4:
                return False
        return True

    @classmethod
    def check_name(cls, name):
        if type(name) != str:
            return False
        name_lst = name.split()
        for id, num in enumerate(name_lst):
            if not all(map(lambda x: x in cls.CHARS_FOR_NAME, (_ for _ in num))) or id == 2:
                return False
        return True


is_number = CardCheck.check_card_number("123-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number)