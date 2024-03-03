from game import game

main_game = game()

while main_game.win_check() == -1:
    print(main_game.get_state())
    main_game.print_board()
    x = int(input("Enter The Move"))
    data = main_game.move(x)
    if(main_game.win_check() == 2):
        print("X wins")
        game.print_board()
        break
    if(main_game.win_check() == 1):
        print("O wins")
        game.print_board()
        break