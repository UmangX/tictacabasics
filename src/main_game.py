import numpy as np 

def generate():
    brd = np.zeros(9)
    return brd
def print_baord(brd):
    for i in range(9): 
        x = i + 1 
        if brd[i] == 0:
            print("_ ",end=' ')
        if brd[i] == 1:
            print("X ",end=' ')
        if brd[i] == 2:
            print("O ",end=' ')
        if (x%3) == 0:
            print()
def move(x,brd):
    brd[x] = 1
def win_check(brd):
    if (brd[0] == brd[4] == brd[8] != 0):
        return brd[0]; 
    if (brd[0] == brd[1] == brd[2] != 0):
        return brd[0]; 
    if (brd[3] == brd[4] == brd[5] != 0):
        return brd[0]; 
    if (brd[6] == brd[7] == brd[8] != 0):
        return brd[0]; 
    if (brd[0] == brd[3] == brd[6] != 0):
        return brd[0]; 
    if (brd[1] == brd[4] == brd[7] != 0):
        return brd[0]; 
    if (brd[2] == brd[5] == brd[8] != 0):
        return brd[0]; 
    if (brd[2] == brd[4] == brd[6] != 0):
        return brd[0]; 
    else:
        return -1 

def get_state(brd):
    a = ""
    for i in range(9):
        a = a + str(int(brd[i]))
    return a;

def state_to_np(state):
    res = np.zeros(9)
    count = 0
    for i in state:
        res[count] = int(i)
        count = count + 1
    return res

tester = generate()

tester_state = "010200120"


while False:
    print_baord(tester)
    mv = int(input("enter the move"))
    move(mv,tester)
    if win_check(tester) == 1:
        print("X wins")
        break
    if(win_check(tester) == 2):
        print("Y winds")
        break