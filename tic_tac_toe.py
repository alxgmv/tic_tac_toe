import random
from IPython.display import clear_output


def tic_tac_toe_board_draw(board):
    clear_output()
    print('--- --- ---')
    print(f'| {board[2][0]} | {board[2][1]} | {board[2][2]} |')
    print('--- --- ---')
    print(f'| {board[1][0]} | {board[1][1]} | {board[1][2]} |')
    print('--- --- ---')
    print(f'| {board[0][0]} | {board[0][1]} | {board[0][2]} |')


def tic_tac_toe_choice():
    '''
    Player 1 chooses X or O
    Second choice = O if Player 1 choose X or X if Player 1 choose O
    '''

    choice = ''
    while choice != 'X' and choice != 'O':
        choice = input('Choose X or O: ').upper()
    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def tic_tac_toe_board_move(board, choice, position):
    row, col = position
    board[row][col] = choice


def winner(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False


def tic_tac_toe_first_move():
    first_move = random.randint(0, 1)
    if first_move == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def tic_tac_toe_empty_space_check(board, position):
    row, col = position
    return board[row][col] == ' '


def tic_tac_toe_board_full_check(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def tic_tac_toe_restart():
    return input('Do you want to play again? Yes or No: ').lower().startswith('y')


def palyer_choice(board):
    position = 0
    while True:
        try:
            position = int(input('Choose your next position: (1-9) '))
            if position in range(1, 10):
                row, col = divmod(position - 1, 3)
                if tic_tac_toe_empty_space_check(board, (row, col)):
                    return (row, col)
            print("Invalid input. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


while True:
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    pl_1, pl_2 = tic_tac_toe_choice()
    turn = tic_tac_toe_first_move()
    print(turn + ' will go first')
    game_on = True
    while game_on:
        if turn == 'Player 1':
            tic_tac_toe_board_draw(board)
            position = palyer_choice(board)
            tic_tac_toe_board_move(board, pl_1, position)
            if winner(board, pl_1):
                tic_tac_toe_board_draw(board)
                print('Player 1 has won!')
                game_on = False
            else:
                if tic_tac_toe_board_full_check(board):
                    tic_tac_toe_board_draw(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            tic_tac_toe_board_draw(board)
            position = palyer_choice(board)
            tic_tac_toe_board_move(board, pl_2, position)
            if winner(board, pl_2):
                tic_tac_toe_board_draw(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if tic_tac_toe_board_full_check(board):
                    tic_tac_toe_board_draw(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not tic_tac_toe_restart():
        break
