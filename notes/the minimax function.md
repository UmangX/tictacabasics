__the main function__

```python

def minimax(state, depth, player):  

# if the player is the computer then the best score is the minimum possible value 
	if player == COMP:
	# if the player is the computer then the score is at the minimum possible value 
	# the value is at the minimum because intially any valid move is better then nothing 
		best = [-1, -1, -infinity]
    else:
	# if the player is the human then the best score is the maximum possible value 
        best = [-1, -1, +infinity]

	# this is the base case when the condition is met it returns a invalid move with the terminal state score 
	# this means the function reached its end and the only score left is the final score 
	if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score] 
		
	# this for loop goes through each empty moves 
    for cell in empty_cells(state):
	# this uses the new valid move and then 
        x, y = cell[0], cell[1]
    # sets the state to the player 
        state[x][y] = player
    # changes the player computer to human choice or human to the minimum computer choice 
    # this is the optimal move assuming the human player chooses the best move meaning the maximum score 
        score = minimax(state, depth - 1, -player)
	# this reverts the state to the clear set 
        state[x][y] = 0
        score[0], score[1] = x, y

        `if player == COMP:`
            `if score[2] > best[2]:`
                `best = score  # max value`
        `else:`
            `if score[2] < best[2]:`
                `best = score  # min value`

    return best

```

__the code for the ai turn that directly uses the min max function__

```python
def ai_turn(c_choice, h_choice):
	
	# depth is the numbers of valid left moves 
	depth = len(empty_cells(board))
	
	# if depth ( numbers of moves left ) and game_over( if either of the player wins)
	if depth == 0 or game_over(board):
		return 

	# clears the console  
	clean()
    print('Computer turn [{}]'.format(c_choice))
    render(board, c_choice, h_choice)

	# if the games is at the start then the valid move would be 
    if depth == 9:
    # choice is the external function from the random lib this selects anyone from the the list 
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
    # when the game has done with the first move the program select the coordinate from the minimax function 
    # move - the best move using the depth variable and the computer as the player 
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

	# the set move makes the move 
    set_move(x, y, COMP)
    time.sleep(1)
```

__dry running the entire thing__

- the function returns the following 
	- a list with the following 
		- x , y and score

- lets the play a game 
	- xox_xxo_o - this is a state 
	- the parameter for the following the minmax is the state,depth,player 