from main_game import *

class node: 
    def __init__(self):
        self.data = None
        self.childrens = []
        self.parent = None 


def generate_next_move(current_state): 
    moves = []
    test_state = current_state
    for i in range(9):
        if test_state[i] == '0':
            new_state = test_state
            new_state = new_state[:i] + '2' + new_state[i+1:]
            moves.append(new_state)
    return moves


# 1 is for the player 2 is for the computer 



print_baord(state_to_np(generate_next_move("121121120")[0])) 