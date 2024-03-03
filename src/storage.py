import numpy as np


# generates array with 9 len which is projected as the board and used for numerical stuff
def generate():
    brd = np.zeros(10)
    brd[9] = 1
    return brd


# prints the np array as a baord
def print_board(brd):
    for i in range(9):
        x = i + 1
        if brd[i] == 0:
            print("_ ", end=" ")
        if brd[i] == 1:
            print("X ", end=" ")
        if brd[i] == 2:
            print("O ", end=" ")
        if (x % 3) == 0:
            print()


# defines a move changes the position value to 1 which is referred to as X
def move(x, brd):
    brd[x] = 1


# check the board with the rows , columns and diagonal return 1 , 2 , -1
def win_check(brd):
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


def generate_moves_for_2(intial_state):
    generated = []
    for i in range(9):
        if intial_state[i] == 0:
            new_state = intial_state.copy()
            new_state[i] = 2
            new_state[9] = 1
            generated.append(new_state)
    return generated


# 2 = O 1 = X 0 = _


def generate_moves_for_1(intial_state):
    generated = []
    for i in range(9):
        if intial_state[i] == 0:
            new_state = intial_state.copy()
            new_state[i] = 1
            new_state[9] = 2
            generated.append(new_state)
    return generated


tester = generate()


class node(object):
    def __init__(self, data, parent):
        self.data = data
        self.children = []
        self.parent = parent

    def add_children(self, obj):
        self.children.append(obj)


def printTree(root, level=0):
    print("  " * level, root.data)
    for child in root.children:
        printTree(child, level + 1)


data_set = node(tester, tester)

# how many possible moves for the game = the length of the state storage

# lets play a game you and i
