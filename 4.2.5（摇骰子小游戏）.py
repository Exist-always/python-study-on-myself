def start_game():
    print('<<<<<<GAME STARTS!>>>>>>')
    choices = ['Big','Small']
    your_choice = input('Big or Small:')
    if your_choice in choices:
        points = roll_dices()
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:
            print('The points are',points,'YOU WIN! ')
        else:
            print('The points are', points,'YOU LOSE!')
    else:
        print('Invaild Words')
        start_game()
start_game()