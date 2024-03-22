from random import randint

state = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
brd.print_any_board(state)


player = "X"
opponent = "O"


def left_moves(state):
    res = []
    inx = int(0)
    for i in state:
        if i == "_":
            res.append(inx)
        inx = inx + 1
    return res


running = False
which_turn = True


def evaluate(state, x):
    tester = state
    tester[x] = "O"
    if brd.check_win(tester, "O"):
        return 10
    if brd.check_win(tester, "X"):
        return -10
    else:
        return 0


while running:

    print("--------------------------------")
    brd.print_any_board(state)

    if which_turn:
        inx = int(input("Enter the Move"))
        if inx in left_moves(state):
            state[inx] = "X"
            which_turn = not which_turn
        else:
            print("Enter a Valid Move")
            continue
    else:
        left = left_moves(state)
        inx = randint(0, len(left))
        state[inx] = "O"
        which_turn = not which_turn

    if brd.check_win(state, "X"):
        print("X WINS")
        running = False
    if brd.check_win(state, "O"):
        print("O WINS")
        running = False
    if len(left_moves(state)) == 0:
        print("No Moves Left")
        running = False
