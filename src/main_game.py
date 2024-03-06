from game import game

main_game = game()

winning_states = []
winning_states.append([2, 2, 2, 0, 0, 0, 0, 0, 0])
winning_states.append([0, 0, 0, 2, 2, 2, 0, 0, 0])
winning_states.append([0, 0, 0, 0, 0, 0, 2, 2, 2])
winning_states.append([2, 0, 0, 2, 0, 0, 2, 0, 0])
winning_states.append([2, 0, 0, 2, 0, 0, 2, 0, 0])
winning_states.append([0, 2, 0, 0, 2, 0, 0, 2, 0])
winning_states.append([0, 0, 2, 0, 0, 2, 0, 0, 2])
winning_states.append([2, 0, 0, 0, 2, 0, 0, 0, 2])
winning_states.append([0, 0, 2, 0, 2, 0, 2, 0, 0])

# make a function that would match the state with the winning state


def matching(d1, d2):
    percentage = 0
    for i in range(9):
        if d1[i] == d2[i]:
            percentage = percentage + 1
    return percentage


# make a function that generate the steps to reach the winning state
def generate_moves(brd):
    moves = []
    if brd.win_check() == 2:
        return moves


for m in winning_states:
    tester_game = game()
    tester_game.set_state(m)
    print("-------------------")
    tester_game.print_board()


def run():
    while main_game.win_check() == -1:

        print(main_game.get_state())
        main_game.print_board()
        x = int(input("Enter The Move"))
        main_game.move(x)
        if main_game.win_check() == 2:
            print("X wins")
            main_game.print_board()
            break
        if main_game.win_check() == 1:
            print("O wins")
            main_game.print_board()
            break
