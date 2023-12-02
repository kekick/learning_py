class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
            self.tail = obj

        elif self.tail:
            prev = self.tail
            self.tail = obj
            self.tail.set_prev(prev)
            prev.set_next(self.tail)

    def remove_obj(self):
        if self.tail:
            if self.tail == self.head:
                self.head = None
                self.tail = None
            self.tail = self.tail.get_prev()


    def get_data(self):
        lst = []
        temp = self.head

        while temp:
            if temp:
                lst.append(temp.get_data())
                temp = temp.get_next()

        return lst


class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data



lst = LinkedList()
lst.add_obj(ObjList("данные 1"))

res = lst.get_data()
print(res)
