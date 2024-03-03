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
        data = main_game.move(x)
        if main_game.win_check() == 2:
            print("X wins")
            main_game.print_board()
            break
        if main_game.win_check() == 1:
            print("O wins")
            main_game.print_board()
            break
