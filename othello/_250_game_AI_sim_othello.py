# Reversegam: a clone of Othello/REversi
import random
import sys

WIDTH = 8
HEIGHT = 8


def draw_board(board):
    """Draws the board given the data from "board"

    Args:
        board (list): list of data coordinates of board and pieces on board
    """
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print(f'{y + 1}|', end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print(f'|{y + 1}')

    print(' +--------+')
    print('  12345678')


def get_new_board():
    """Create a brand-new, blank board data structure.

    Returns:
        list: blank board data structure
    """
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def get_board_copy(board):
    """Creates a copy of passed "board"

    Args:
        board (list): list of data coordinates of board and pieces on board

    Returns:
        list: Copy of board data structure
    """
    # Make a duplicate of the board list and return it.
    board_copy = get_new_board()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board_copy[x][y] = board[x][y]

    return board_copy


def is_valid_move(board, tile, x_start, y_start):
    """Checks to see if move is valid

    Args:
        board (list): list of data coordinates of board and pieces on board
        tile (string): String of character to be placed on board
        x_start (int): x coordinates
        y_start (int): y coordinates

    Returns:
        If it is a valid move, return a list of spaces that would become the player's if they made a move here.
        Return False if the player's move on space xstart, ystart is invalid.
    """
    test = is_on_corner(x_start, y_start)
    if board[x_start][y_start] != ' ' or not is_on_board(x_start, y_start):
        return False

    if tile == 'X':
        other_tile = 'O'
    else:
        other_tile = 'X'

    tiles_to_flip = []
    for x_direction, y_direction in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = x_start, y_start
        # First step in the x direction
        x += x_direction
        # First step in the y direction
        y += y_direction

        while is_on_board(x, y) and board[x][y] == other_tile:
            # Keep moving in this x & y direction.
            x += x_direction
            y += y_direction
            if is_on_board(x, y) and board[x][y] == tile:
                # There are pieces to flip over.  Go in reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= x_direction
                    y -= y_direction
                    if x == x_start and y == y_start:
                        break
                    tiles_to_flip.append([x, y])

    # If no tiles were flipped, this is not a valid move.
    if len(tiles_to_flip) == 0:
        return False
    return tiles_to_flip


def get_valid_moves(board, tile):
    """Gets a list of valid moves

    Args:
        board (list): list of data coordinates of board and pieces on board
        tile (string): String of character to be placed on board

    Returns:
        list: lists of valid moves for the given player on the given board
    """
    valid_moves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_valid_move(board, tile, x, y) != False:
                valid_moves.append([x, y])

    return valid_moves


def is_on_board(x, y):
    """Checks to see if coordinates are on the board

    Args:
        x (int): x coordinates
        y (int): y coordinates

    Returns:
        bool: Return True if the coordinates are located on the board.
    """
    # Return True if the coordinates are located on the board.
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1


def get_board_with_valid_moves(board, tile):
    """Gets board with all valid moves

    Args:
        board (list): list of data coordinates of board and pieces on board
        tile (string): String of character to be placed on board

    Returns:
        Return a new board with periods making the valid moves the player can make.
    """
    board_copy = get_board_copy(board)

    for x, y in get_valid_moves(board_copy, tile):
        board_copy[x][y] = '.'

    return board_copy


def get_score_of_board(board):
    """Determine the score by counting the tiles

    Args:
        board (list): list of data coordinates of board and pieces on board

    Returns:
        dict: A dictionary with keys 'X' and 'O'
    """
    x_score = 0
    o_score = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                x_score += 1
            if board[x][y] == 'O':
                o_score += 1

    return ({'X': x_score, 'O': o_score})


def enter_player_tile():
    """Get what tile player wants to use

    Returns:
        list: Return a list with the player's tile as the first item and the computer's tile as the second.
    """
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    # The first elment in the list is the player's tile, and the second is the computer's tile
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    """Randomly chooses who goes first

    Returns:
        string: Player who goes first
    """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def make_move(board, tile, x_start, y_start):
    """Place the tile on the board at xstart, ystart and flip any of the opponents's pieces

    Args:
        board (list): list of data coordinates of board and pieces on board
        tile (string): String of character to be placed on board
        x_start (int): x coordinates
        y_start (int): y coordinates

    Returns:
        bool: Return Flase if this is an invalid move; True if it is valid
    """
    tiles_to_flip = is_valid_move(board, tile, x_start, y_start)

    if tiles_to_flip == False:
        return False

    board[x_start][y_start] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile

    return True


def is_on_corner(x, y):
    """Checks to see if move is in the corner of board

    Args:
        x (int): x coordinates
        y (int): y coordinates

    Returns:
        bool: Return True if the position is in one of the four corners
    """
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def get_player_move(board, player_tile):
    """Let the player enter their move

    Args:
        board (list): list of data coordinates of board and pieces on board
        player_tile (string): string of players tile

    Returns:
        Return the move as [x, y] (or return the strings 'hints' or 'quit')
    """
    DIGITS_1_TO_8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move

        if len(move) == 2 and move[0] in DIGITS_1_TO_8 and move[1] in DIGITS_1_TO_8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if is_valid_move(board, player_tile, x, y) == False:
                continue
            else:
                break
        else:
            print('This is not a valid move.  Enter the column (1-8) and then row (1-8).')
            print('For example 81 will move on the top-right corner.')

    return [x, y]


def get_computer_move(board, cpu_tile):
    """[summary]

    Args:
        board (list): list of data coordinates of board and pieces on board
        cpu_tile (string): string of computers tile

    Returns:
        list: Return the move as [x, y]
    """
    possible_moves = get_valid_moves(board, cpu_tile)
    # Randomize the order of the moves.
    random.shuffle(possible_moves)

    # Always go for a corner if available.
    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]

    # Find the highest-scoring move possible.
    best_score = -1
    for x, y in possible_moves:
        board_copy = get_board_copy(board)
        make_move(board_copy, cpu_tile, x, y)
        score = get_score_of_board(board_copy)[cpu_tile]
        if score > best_score:
            best_move = [x, y]
            best_score = score

    return best_move


def print_score(board, player_tile, cpu_tile):
    """Prints the current score of passed "board"

    Args:
        board (list): list of data coordinates of board and pieces on board
        player_tile (string): string of players tile
        cpu_tile (string): string of computers tile
    """
    score = get_score_of_board(board)
    print(
        f'You: {score[player_tile]} points.  Computer {score[cpu_tile]} points.')


def play_game(player_tile, cpu_tile):
    """Main game function.  Runs all helper functions from hiere

    Args:
        player_tile (string): string of players tile
        cpu_tile (string): string of computers tile

    Returns:
        Returns a board after a player has made its move
    """
    show_hints = False
    turn = who_goes_first()
    print(f'The {turn} will go first.')

    # Clear the board and place starting pieces.
    game_board = get_new_board()
    game_board[3][3] = 'X'
    game_board[3][4] = 'O'
    game_board[4][3] = 'O'
    game_board[4][4] = 'X'

    while True:
        player_valid_moves = get_valid_moves(game_board, player_tile)
        cpu_valid_moves = get_valid_moves(game_board, cpu_tile)

        if player_valid_moves == [] and cpu_valid_moves == []:
            # No one can move, so end the game.
            return game_board
        # Player's turn
        elif turn == 'player':
            if player_valid_moves != []:
                # if show_hints:
                #     valid_moves_board = get_board_with_valid_moves(
                #         game_board, player_tile)
                #     draw_board(valid_moves_board)
                # else:
                #     draw_board(game_board)
                # print_score(game_board, player_tile, cpu_tile)

                move = get_computer_move(game_board, player_tile)
                # if move == 'quit':
                #     print('Thanks for playing!')
                #     sys.exit()
                # elif move == 'hints':
                #     show_hints = not show_hints
                #     continue
                # else:
                make_move(game_board, player_tile, move[0], move[1])

            turn = 'computer'
        # Computer's turn
        elif turn == 'computer':
            if cpu_valid_moves != []:
                # draw_board(game_board)
                # print_score(game_board, player_tile, cpu_tile)

                # input("Press Enter to see the computer's move.")
                move = get_computer_move(game_board, cpu_tile)
                make_move(game_board, cpu_tile, move[0], move[1])

            turn = 'player'


NUM_GAMES = 250
xWins = oWins = ties = 0
print('Welcome to Reversegam!')

player_tile, cpu_tile = ['X', 'O']

for i in range(NUM_GAMES): # while True:
    final_board = play_game(player_tile, cpu_tile)

    # Display the final score
    # draw_board(final_board)
    scores = get_score_of_board(final_board)
    print(f"#{i + 1}: X scored {scores['X']} points. O scored {scores['O']} points.")
    if scores[player_tile] > scores[cpu_tile]:
      xWins += 1
        # print(
        #     f'You beat the computer by {scores[player_tile] - scores[cpu_tile]} points! Congratulations!')
    elif scores[player_tile] < scores[cpu_tile]:
      oWins += 1
        # print(
        #     f'You lost.  The computer beat you by {scores[cpu_tile] - scores[player_tile]} points.')
    else:
      ties += 1
        # print('The game ended in a tie!')

    # print('Do you want to play again? (yes or no)')
    # if not input().lower().startswith('y'):
    #     break

print(f'X wins: {xWins} {round(xWins / NUM_GAMES * 100, 1)}')
print(f'O wins: {oWins} {round(oWins / NUM_GAMES * 100, 1)}')
print(f'Ties: {ties} {round(ties / NUM_GAMES * 100, 1)}')
