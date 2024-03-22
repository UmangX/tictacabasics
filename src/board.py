# create a stable game for managing the state
import numpy as np


class Board:

    def __init__(self, brd=None, timeline=None):
        self.brd = np.zeros(10)
        self.timeline = []
        self.brd[9] = 1

    def set_state(self, new_data):
        for i in range(9):
            self.brd[i] = new_data[i]

    # 1 == X , 2 == O
    def get_state(self):
        return self.brd

    def print_board(self):
        for i in range(9):
            x = i + 1
            if self.brd[i] == 0:
                print("_ ", end=" ")
            if self.brd[i] == 1:
                print("X ", end=" ")
            if self.brd[i] == 2:
                print("O ", end=" ")
            if (x % 3) == 0:
                print()

    def print_any_board(state):
        for i in range(9):
            x = i + 1
            print(state[i], end=" ")
            if (x % 3) == 0:
                print()

    def move(self, x):
        is_move_left = False
        is_movable = False
        for i in self.get_empty():
            if i == x:
                is_movable = True
        if not is_movable:
            print("Enter a valid State")
            return False

        for i in self.brd:
            if i == 0:
                is_move_left = True
        if self.brd[9] == 1:
            self.brd[x] = 1
            self.brd[9] = 2
            self.timeline.append([1, x])
            return is_move_left
        if self.brd[9] == 2:
            self.brd[x] = 2
            self.brd[9] = 1
            self.timeline.append([2, x])
            return is_move_left

    def get_empty(self):
        empty = []
        for i in range(9):
            if self.brd[i] == 0:
                empty.append(i)
        return empty

    def get_timeline(self):
        return self.timeline

    def get_next_player(self):
        return self.brd[9]

    def is_draw(self):
        lst = self.get_empty()
        if self.win_check() == -1 and len(lst) == 0:
            return True
        return False

    def win_check(self):
        brd = self.brd
        if brd[0] == brd[4] == brd[8] != 0:
            return brd[0]
        if brd[0] == brd[1] == brd[2] != 0:
            return brd[0]
        if brd[3] == brd[4] == brd[5] != 0:
            return brd[0]
        if brd[6] == brd[7] == brd[8] != 0:
            return brd[0]
        if brd[0] == brd[3] == brd[6] != 0:
            return brd[0]
        if brd[1] == brd[4] == brd[7] != 0:
            return brd[0]
        if brd[2] == brd[5] == brd[8] != 0:
            return brd[0]
        if brd[2] == brd[4] == brd[6] != 0:
            return brd[0]
        else:
            return -1

    def check_win(state, x):
        brd = state
        if brd[0] == brd[4] == brd[8] == x:
            return True
        if brd[0] == brd[1] == brd[2] == x:
            return True
        if brd[3] == brd[4] == brd[5] == x:
            return True
        if brd[6] == brd[7] == brd[8] == x:
            return True
        if brd[0] == brd[3] == brd[6] == x:
            return True
        if brd[1] == brd[4] == brd[7] == x:
            return True
        if brd[2] == brd[5] == brd[8] == x:
            return True
        if brd[2] == brd[4] == brd[6] == x:
            return True
        else:
            return False
