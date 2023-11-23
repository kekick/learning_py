class Graph:

    def __init__(self, data, is_show=True):
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data):
        self.data = data.copy()

    def show_table(self):
        if self.is_show:
           print(*self.data)
        else:
            print("Отображение данных закрыто")


    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {*self.data,}")
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма:", *self.data)
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show



numbers = [1, 2, 3]
print(f"Числа: {*numbers,}")
