class ListObject:

    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = ['1. Первые шаги в ООП',
       '1.1 Как правильно проходить этот курс',
       '1.2 Концепция ООП простыми словами',
       '1.3 Классы и объекты. Атрибуты классов и объектов',
       '1.4 Методы классов. Параметр self',
       '1.5 Инициализатор init и финализатор del',
       '1.6 Магический метод new. Пример паттерна Singleton',
       '1.7 Методы класса (classmethod) и статические методы (staticmethod)]'
          ]

for i, k in enumerate(lst_in):
    if i == 0:
        head_obj = ListObject(k)
        if i < len(lst_in)-1:
            head_obj.link(ListObject(lst_in[i + 1]))
            temp = head_obj.next_obj
    else:
        if i < len(lst_in)-1:
            temp.link(ListObject(lst_in[i + 1]))
            temp = temp.next_obj



