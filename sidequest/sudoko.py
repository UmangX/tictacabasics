import numpy as np


class suduko:
    def __init__(self, brd=None):
        self.brd = np.zeros((9, 9)).astype(int)

    def print_brd(self):
        for i in range(9):
            print()
            for j in range(9):
                print(self.brd[i][j], end=" ")

    def set_game(self, pre_game):
        for i in range(9):
            for j in range(9):
                self.brd[i][j] = pre_game[i][j]

    def is_avail_row(self, x, tar):
        for i in range(9):
            if self.brd[x][i] == tar:
                return False
        return True

    def is_avail_col(self, x, tar):
        for i in range(9):
            if self.brd[i][x] == tar:
                return False
        return True

    def is_aviable(self, x, y, tar):
        if self.is_avail_col(x, tar) and self.is_avail_row(y, tar):
            return True
        return False

    def play_game(self):
        for x in range(9):
            for y in range(9):
                if self.brd[x][y] == 0:
                    for i in range(10):
                        if i != 0:
                            if self.is_aviable(x, y, i):
                                self.brd[x][y] = i


defaultgrid = [
    [0, 0, 4, 0, 6, 0, 0, 0, 5],
    [7, 8, 0, 4, 0, 0, 0, 2, 0],
    [0, 0, 2, 6, 0, 1, 0, 7, 8],
    [6, 1, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 7, 5, 4, 0, 0, 6, 1],
    [0, 0, 1, 7, 5, 0, 9, 3, 0],
    [0, 7, 0, 3, 0, 0, 0, 1, 0],
    [0, 4, 0, 2, 0, 6, 0, 0, 7],
    [0, 2, 0, 0, 0, 7, 4, 0, 0],
]

if __name__ == "__main__":
    play = suduko()
    play.set_game(defaultgrid)
    play.print_brd()
    print()
    print("after playing")
    play.play_game()
    play.print_brd()
