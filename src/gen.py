from main_game import *

class node: 
    def __init__(self):
        self.data = None
        self.childrens = []
        self.parent = None 

#improve this for multiplayer this generates single state 
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

#this use np array instead of string
def generate_moves(intial_state):
    generated = []
    for i in range(9):
        if intial_state[i] == 0:
            new_state = intial_state.copy()
            new_state[i] = 2
            generated.append(new_state)
    return generated 

tester_brd = generate()
move(1,tester_brd)
move(2,tester_brd)
move(3,tester_brd)
move(4,tester_brd)
move(8,tester_brd)
print_board(tester_brd) 

