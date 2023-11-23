import random


class Cell:

    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:

    def __init__(self, size, mines_total):
        self.pole = [[Cell() for _ in range(size)] for _ in range(size)]
        self.M = mines_total
        self.N = size

    def init(self):
        mines = random.sample(range(self.N ** 2), self.M)
        for mine in mines:
            x, y = divmod(mine, self.N)
            self.pole[x][y].mine = True
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.N and 0 <= ny < self.N:
                        self.pole[nx][ny].around_mines += 1

    def show(self):
        for row in self.pole:
            for cell in row:
                if cell.around_mines != 0:
                    cell.fl_open = True
                if cell.fl_open:
                    print(cell.around_mines if not cell.mine else '*', end='  ')
                else:
                    print('#', end='  ')
            print()

pole_game = GamePole(10, 12)
pole_game.init()
pole_game.show()