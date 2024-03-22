import numpy as np
from math import inf
import os
import time

human, computer = -1, 1
cross, nought = "X", "O"

state = np.zeros(9)


def print_state(state):
    for i in range(9):
        counter = i + 1
        if state[i] == -1:
            print(cross + " ", end=" ")
        if state[i] == 1:
            print(nought + " ", end=" ")
        if state[i] == 0:
            print("_ ", end=" ")
        if counter % 3 == 0:
            print()


def win_check(brd):
    if brd[0] == brd[4] == brd[8] and brd[0] != 0:
        return brd[0]
    if brd[0] == brd[1] == brd[2] and brd[0] != 0:
        return brd[0]
    if brd[3] == brd[4] == brd[5] and brd[3] != 0:
        return brd[0]
    if brd[6] == brd[7] == brd[8] and brd[6] != 0:
        return brd[0]
    if brd[0] == brd[3] == brd[6] and brd[0] != 0:
        return brd[0]
    if brd[1] == brd[4] == brd[7] and brd[1] != 0:
        return brd[0]
    if brd[2] == brd[5] == brd[8] and brd[2] != 0:
        return brd[0]
    if brd[2] == brd[4] == brd[6] and brd[2] != 0:
        return brd[0]
    else:
        return 0


def game_over(state):
    if win_check(state) != 0:
        return False
    return True


def empty_pos(state):
    move = []
    for i in range(9):
        if state[i] == 0:
            move.append(i)
    return move


def evaluate(state):
    return win_check(state)


def minmax(state, depth, player):
    if player == computer:
        best = [-1, -inf]
    if player == human:
        best = [-1, inf]
    if depth == 0 or win_check(state):
        final_score = evaluate(state)
        return [-1, final_score]
    for x in empty_pos(state):
        state[x] = player
        score = minmax(state, depth - 1, -player)
        state[x] = 0
        score[0] = x
        if player == computer:
            if score[1] > best[1]:
                best = score
        else:
            if score[1] < best[1]:
                best = score
    return best


player = human


def clear():
    os.system("cls" if os.name == "nt" else "clear")


while True:

    if player == computer:
        depth = len(empty_pos(state))
        comp_move = minmax(state, depth, computer)
        state[comp_move[0]] = computer
        clear()
        print_state(state)
        print(empty_pos(state))
        time.sleep(1)
        if win_check(state) == human:
            print("you won")
            break
        if win_check(state) == computer:
            print("computer won")
            break
        player = -player

    if player == human:
        ins = int(input("Enter the move"))
        if ins in empty_pos(state):
            state[ins] = human
        else:
            ins = int(input("Enter a valid move"))
            state[ins] = human
        clear()
        print_state(state)
        print(empty_pos(state))
        if win_check(state) == human:
            print("you won")
            break
        if win_check(state) == computer:
            print("computer won")
            break
        player = -player

    depth = len(empty_pos(state))
    if depth == 0:
        print("NO MOVES LEFT")
        break

    if game_over(state):
        print("Game Over")
        if win_check(state) == human:
            print("YOU WON")
            break
        if win_check(state) == computer:
            print("COMPUTER WON")
            break
