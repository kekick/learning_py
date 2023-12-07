# class Car:
#
#     def __init__(self):
#         self.__model = None
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if isinstance(model, str) and 1 < len(model) < 101:
#             self.__model = model


"""________________________________________________________________________________________________________________"""

#
# class WindowDlg:
#
#     def __init__(self, title, widht, height):
#         self.__title = title
#         self.__width = widht
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         if isinstance(width, int) and -1 < width < 10000:
#             self.__width = width
#             self.show()
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         if isinstance(height, int) and -1 < height < 10000:
#             self.__height = height
#             self.show()
#
#     def show(self):
#         print(f"{self.__title}: {self.__width}, {self.__height}")
#

"""________________________________________________________________________________________________________________"""

'''_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-STACK_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_'''

#
# class StackObj:
#
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, next_obj):
#         if isinstance(next_obj, StackObj) or next_obj is None:
#             self.__next = next_obj
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#
# class Stack:
#
#     def __init__(self):
#         self.top = None
#         self.obj = None
#
#     def push(self, obj):
#         if isinstance(obj, StackObj):
#             if self.top is None:
#                 self.top = obj
#                 self.obj = obj
#             elif self.top and self.top.next is None:
#                 self.top.next = obj
#                 self.obj = obj
#             else:
#                 self.obj.next = obj
#                 self.obj = obj
#
#     def pop(self):
#         if self.top is None:
#             return None
#         else:
#             temp = self.top
#             if temp.next:
#                 while temp.next is not None:
#                     prev = temp
#                     temp = temp.next
#                 prev.next = None
#                 self.obj = prev
#             else:
#                 self.top = None
#         return temp
#
#     def get_data(self):
#         lst = []
#         x = 1
#         temp = self.top
#         while x:
#             if temp:
#                 lst.append(self.top.data)
#                 x = temp.next
#                 temp = None
#             elif self.top is None:
#                 break
#             else:
#                 lst.append(x.data)
#                 x = x.next
#         return lst
#

# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()
# # print(res)
# s = Stack()
# for i in range(10):
#     s.push(StackObj(f'none obj {i}'))
#     print(s.get_data())
#
# for i in range(11):
#     a = s.pop()
#     print(a, "____", s.get_data())

"""________________________________________________________________________________________________________________"""

"""__________________________________________RADIUS_VECTOR2D_______________________________________________________"""
#
#
# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024
#
#     def __init__(self, x=0, y=0):
#         self.__x = x if self.coord_checker(x) else 0
#         self.__y = y if self.coord_checker(y) else 0
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if self.coord_checker(x):
#             self.__x = x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         if self.coord_checker(y):
#             self.__y = y
#
#     @classmethod
#     def coord_checker(cls, coord):
#         return isinstance(coord, (int, float)) and cls.MIN_COORD - 1 < coord < cls.MAX_COORD + 1
#
#     @staticmethod
#     def norm2(vector):
#         if isinstance(vector, RadiusVector2D):
#             return vector.x ** 2 + vector.y ** 2


"""________________________________________________________________________________________________________________"""

"""_______________________________________________BINARY_TREE______________________________________________________"""
#
# class TreeObj:
#     def __init__(self, indx, value=None):
#         self.indx = indx
#         self.value = value
#         self.__left = None
#         self.__right = None
#
#     @property
#     def left(self):
#         return self.__left
#
#     @left.setter
#     def left(self, obj):
#         self.__left = obj
#
#     @property
#     def right(self):
#         return self.__right
#
#     @right.setter
#     def right(self, obj):
#         self.__right = obj
#
#
# class DecisionTree:
#     @classmethod
#     def add_obj(cls, obj, node=None, left=True):
#         if node is None:
#             return obj
#         else:
#             if left:
#                 node.left = obj
#             else:
#                 node.right = obj
#             return obj
#     @classmethod
#     def predict(cls, root, x):
#
#         temp = root
#         while temp.value is None:
#             if x[temp.indx] == 1:
#                 temp = temp.left
#             else:
#                 temp = temp.right
#         return temp.value

"""________________________________________________________________________________________________________________"""

"""_______________________________________________PATH_LINES_______________________________________________________"""
#
#
# class LineTo:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class PathLines:
#
#     def __init__(self, *args):
#         self.path = [LineTo(0, 0)] + list(args) if args else []
#
#     def get_path(self):
#         return self.path
#
#     def get_length(self):
#         sum = 0
#         for i in range(len(self.path) - 1):
#             sum += ((self.path[i + 1].x - self.path[i].x) ** 2 + (self.path[i + 1].y - self.path[i].y) ** 2) ** 0.5
#         return sum
#
#     def add_line(self, line):
#         self.path.append(line)
#
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# print(dist)

"""________________________________________________________________________________________________________________"""

"""_______________________________________________PHONE_BOOK_______________________________________________________"""


class PhoneBook:

    def __init__(self):
        self.numbers = []

    def add_phone(self, phone):
        self.numbers.append(phone)

    def remove_phone(self, indx):
        self.numbers.pop(indx)

    def get_phone_list(self):
        return self.numbers


class PhoneNumber:

    def __init__(self, number, fio):
        self.number = number if self.chek_number(number) else None
        self.fio = fio if isinstance(fio, str) else None

    @staticmethod
    def chek_number(number):
        return 10000000000 <= number <= 99999999999


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones[0].fio)
