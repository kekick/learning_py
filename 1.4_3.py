class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus in self.tr[eng]:
            pass
        else:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, None)

    def translate(self, eng):
        return self.tr.get(eng)


# здесь создавайте объект класса Translator
tr = Translator()
t = (
    ("tree", "дерево"),
    ('car', 'машина'),
    ('car', 'автомобиль'),
    ('leaf', 'лист'),
    ('river', 'река'),
    ('go', 'идти'),
    ('go', 'ехать'),
    ('go', 'ходить'),
    ('milk', 'молоко')
)
for i, k in t:
    tr.add(i, k)

tr.remove('car')
print(*tr.translate('go'))
