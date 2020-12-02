# Tic-Tac-Toe

import random


def draw_board(board):
    """This function prints out the board that it was passed

    Args:
        board (list of strings): the list of strings represents the board.  Ignore idex 0
    """
    # "board" is a list of
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' -+---+-')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' -+---+-')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def input_player_letter():
    """Lets the player pick which letter they want to be.
     Returns:
          list: with the player's letter as the first item, cpu as the second.
    """
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # The first element in the list is the player's letter, second is the CPU
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    """Randomly selects which player goes first

    Returns:
        string: player who goes first
    """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    """Checks to see if theres a winner from given board and player letter.

    Args:
        board (list of strings): the board at its current state
        letter (string): letter of the player we are checking to see if they won the game

    Returns:
        bool: Returns true is player has won the game
    """

    check_results = []

    #  Create a new array with all possible winning combinations
    for col in range(1, 4):
        row = 3 * (col - 1)
        check_results.append(board[row + 1] + board[row + 2] + board[row + 3])
        check_results.append(board[col] + board[col + 3] + board[col + 6])

    check_results.append(board[1] + board[5] + board[9])
    check_results.append(board[3] + board[5] + board[7])
    return letter * 3 in check_results


def get_board_copy(board):
    """Make a copy of the board list and return it

    Args:
        board (list): list of strings of player moves

    Returns:
        list: copy of passed board
    """
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move):
    """Return true if the passed move is free on the passed board

    Args:
        board (list): list of strings of player moves
        move (int): move player is trying to make

    Returns:
        bool: Check to see if space is open
    """
    return board[move] == ' '


def get_player_move(board):
    """Gets players move

    Args:
        board (list): list of strings of player moves

    Returns:
        int: player move
    """
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def choose_random_move_from_list(board, move_list):
    """Returns a valid move from the passed list on the passed board
       Returns None if there is no valid move

    Args:
        board (list): list of strings of player moves
        move_list (list): list of possible moves
    """
    possible_moves = []
    for i in move_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    """Given a board and the computer's letter, determine where to move and return that move.

    Args:
        board (list): list of strings of player moves
        computer_letter (string): Computer playing letter

    Returns:
        int: Computers move
    """
    if computer_letter == 'X':
        player_letter = '0'
    else:
        player_letter = 'X'

    # Here is the algorithm for our Tic-Tac-Toe AI:
    # First, check if we can win in the next move.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i

    # Check if the player could win on the their next move and block them.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the cetner if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    """Return True if every space on the board has been taken.  Otherwise return False.

    Args:
        board (list): list of strings of player moves

    Returns:
        bool: If the game has ended in a draw
    """
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Welcome to Tic-Tac-Toe')

while True:
    # Reset the board.
    game_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print(f'The {turn} will go first.')
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn
            draw_board(game_board)
            move = get_player_move(game_board)
            make_move(game_board, player_letter, move)

            if is_winner(game_board, player_letter):
                draw_board(game_board)
                print('Hooray! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print("It's a cat's game.")
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn
            move = get_computer_move(game_board, computer_letter)
            make_move(game_board, computer_letter, move)

            if is_winner(game_board, computer_letter):
                draw_board(game_board)
                print('The computer has beaten you!  You lose.')
                game_is_playing = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print('Game has ended in a tie.')
                    break
                else:
                    turn = 'player'

    print('Would you like to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
