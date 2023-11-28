# Здесь объявляется класс Factory
class Factory:

    def build_sequence(self):
        return []

    def build_number(self, string):
        string = string.strip()
        str_lst = list(string)
        sym_count = 0
        for i in str_lst:
            if i.isdigit():
                sym_count += 1
        if str_lst.count('-') > 1 or str_lst.count('.') > 1:
            return None
        elif str_lst.count('.') + str_lst.count('-') + sym_count == len(string):
            string = string.lstrip('0')
            number = float(string)
            return number





class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
print(res)