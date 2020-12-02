# Tic-Tac-Toe

import random


def draw_board(board):
    """This function prints out the board that it was passed

    Args:
        board (list of strings): the list of strings represents the board.  Ignore idex 0
    """
    # "board" is a list of
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-+-+-')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-+-+-')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def input_player_letter():
    """Lets the player pick which letter they want to be.
     Returns:
          list: with the player's letter as the first item, cpu as the second.
    """
    letter = ''
    while not(letter == 'X' or leter == 'O'):
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
    return (
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[7] == letter and board[4] == letter and board[1] == letter) or
        (board[8] == letter and board[5] == letter and board[2] == letter) or
        (board[9] == letter and board[6] == letter and board[3] == letter) or
        (board[7] == letter and board[5] == letter and board[3] == letter) or
        (board[9] == letter and board[5] == letter and board[1] == letter)
    )
