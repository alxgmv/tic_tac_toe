import random
from IPython.display import clear_output


# drawing the board for playing
def tic_tac_toe_board_draw(board):
    clear_output()
    print('--- --- ---')
    print(f'| {board[2][0]} | {board[2][1]} | {board[2][2]} |')
    print('--- --- ---')
    print(f'| {board[1][0]} | {board[1][1]} | {board[1][2]} |')
    print('--- --- ---')
    print(f'| {board[0][0]} | {board[0][1]} | {board[0][2]} |')

# players are choosing X or O


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

# placing the choice on the board


def tic_tac_toe_board_move(board, choice, position):
    row, col = position  # getting the row and column
    board[row][col] = choice

# defining the win condition


def winner(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:  # checking rows
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:  # checking columns
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:  # checking diagonals
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:  # checking diagonals
        return True
    return False

# randomly choosing who goes first


def tic_tac_toe_first_move():
    first_move = random.randint(0, 1)
    if first_move == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# checking if the space is empty


def tic_tac_toe_empty_space_check(board, position):
    row, col = position
    return board[row][col] == ' '

# checking if the board is full


def tic_tac_toe_board_full_check(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

# asking if players want to play again


def tic_tac_toe_restart():
    return input('Do you want to play again? Yes or No: ').lower().startswith('y')

#  player's move on the board according to the numbers on the numpad on the keyboard


def palyer_choice(board):
    position = 0
    while True:
        try:
            position = int(input('Choose your next position: (1-9) '))  # 1-9
            if position in range(1, 10):
                # calculating the row and column
                row, col = divmod(position - 1, 3)
                # checking if the space is empty
                if tic_tac_toe_empty_space_check(board, (row, col)):
                    return (row, col)
            print("Invalid input. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


#   main code
while True:
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [
        ' ', ' ', ' ']]  # initializing the board
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
