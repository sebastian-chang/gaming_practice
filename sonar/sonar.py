# Sonar Treasure Hunt

import random
import sys
import math


def get_new_board():
    """Create a new 60x15 board data structure.
    """
    board = []
    for x in range(60):
        # The main list is a list of 60 lists
        board.append([])
        for y in range(15):
            # Each list in the main list has 15 signle character strings.
            # Use different characters for the ocean to make it more readable.
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')

    return board


def draw_board(board):
    """Draw the board data structure

    Args:
        board (list): list of coords of chests and sonar devices
    """
    # Inital space for the numbers down the left side of the board
    tens_digits_line = '    '
    for i in range(1, 6):
        tens_digits_line += (' ' * 9) + str(i)

    # Print the numbers across the top of the board.
    print(tens_digits_line)
    print('    ' + ('0123456789' * 6))
    print()

    # Print each of the 15 rows.
    for row in range(15):
        # Single-digit numbers need to be padded with an extra space.
        if row < 10:
            extra_space = ' '
        else:
            extra_space = ''

        # Create the string for this row on the board.
        board_row = ''
        for col in range(60):
            board_row += board[col][row]

        print(f'{extra_space}{row} {board_row} {row}')

    # Print the numbers across the bottom of the board.
    print()
    print('    ' + ('0123456789' * 6))
    print(tens_digits_line)


def get_random_chests(num_chests):
    """Creates randomly located chests on game board

    Args:
        num_chests (int): number of chests a player needs to find

    Returns:
        list: List of chests for player to find
    """
    # Create a list of chest data structures (two-item liists of x, y int coords)
    chests = []
    while len(chests) < num_chests:
        new_chest = [random.randint(0, 59), random.randint(0, 14)]
        # Make sure a chest is not already in that position.
        if new_chest not in chests:
            chests.append(new_chest)

    return chests


def is_on_board(x, y):
    """Determines if coords are on the game board

    Args:
        x (int): coords on the x-axis of the board
        y (int): coords on the y-axis of the board

    Returns:
        bool: Return true if the coords are on the board, otherwise false
    """
    # Return true if the coords are on the board, otherwise false
    return x >= 0 and x <= 59 and y >= 0 and y <= 14


def make_move(board, chests, x, y):
    """Chanage the board data structure with a sonar device character.
    Remove treasure chests from the chests list as they are found.

    Args:
        board (list): list of coords of chests and sonar devices
        chests (list): List of chests for player to find
        x (int): coords on the x-axis of the board
        y (int): coords on the y-axis of the board

    Returns:
        Return False if this is an invalid move. Otherwise, return the string of the result of this move.
    """
    # Any chest will be closer than 100.
    smallest_distance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        # We want the closest treasure chests
        if distance < smallest_distance:
            smallest_distance = distance

    smallest_distance = round(smallest_distance)

    if smallest_distance == 0:
        # xy is directly on a treasure chest!
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallest_distance < 10:
            board[x][y] = str(smallest_distance)
            return f'Treasure detected at a distance of {smallest_distance} from the sonar device.'
        else:
            board[x][y] = 'X'
            return 'Sonar did not detect anything.  All treasure chests out of range.'


def enter_player_move(previous_moves):
    """Let the player enter their move.  Return a two-item list of int xy coords.

    Args:
        previous_moves (list): List of previous moves by player

    Returns:
        list: two item list of xy coords
    """
    print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_on_board(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previous_moves:
                print('You already moved there.')
                continue
            return [int(move[0]), int(move[1])]

        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')


def show_instructions():
    """Creates on screen instructions for player if requested
    """
    print('''Instructions:
    You are the captain of the Simon, a treasure-hunting ship.  Your current mission is
    to use sonar devices to find three sunken treasure chests at the bottom of the ocean.
    But you only have cheap sonar that finds distance, not direction.

    Enter the coordinates to drop a sonar device.  The ocean map will be marked with
    how far away the nearest chest is, or an 'X' if it beyond the sonar device's range.
    For example, the 'C' marks are where chests are.  The sonar device shows '3' because
    the closests chest is 3 spaces away.

                1         2         3
    012345678901234567890123456789012

    0~```~~~```~~~``~~~~```~~``~~`~``0
    1~~~~``~~~~`~~````~~~```~~~~`~`~~1
    2~``C~~3~```~~C``~~~~```~~``~~`~`2
    3~~``~~~~``~``~~~~~~~~~``~``~`~`~3
    4~~~~``~~~~`~~C``~~~```~~~~`~`~~`4

    012345678901234567890123456789012
                1         2         3

    (In the real game, the chests are not visible in the ocean.)

    Press enter to continue...''')
    input()

    print('''    When you drop a sonar device directly on a chest, you retrieve it and the
    other sonar devices update to show how far away the next nearest chest is.  The chests
    are beyond the range of the sonar device on the left, so it shows an 'X'.

                1         2         3
    012345678901234567890123456789012

    0~```~~~```~~~``~~~~```~~``~~`~``0
    1~~~~``~~~~`~~````~~~```~~~~`~`~~1
    2~``X~~7~```~~C``~~~~```~~``~~`~`2
    3~~``~~~~``~``~~~~~~~~~``~``~`~`~3
    4~~~~``~~~~`~~C``~~~```~~~~`~`~~`4

    012345678901234567890123456789012
                1         2         3
    The treasure chests don't move around.  Sonar devices can detect treasure chests up to
    a distance of 9 sapces.  Try to collect all 3 chests before running out of sonar devices.
    Good luck!

    Pres enter to continue...''')
    input()


print('S O N A R !')
print()
print('Would you like to view the intrustions? (yes/no)')
if input().lower().startswith('y'):
    show_instructions()

while True:
    # Game setup
    sonar_devices = 20
    the_board = get_new_board()
    the_chests = get_random_chests(3)
    draw_board(the_board)
    previous_moves = []

    while sonar_devices > 0:
            # Show sonar devices and chest statuses
        print(
            f'You have {sonar_devices} sonar device(s) left.  {len(the_chests)} treasure chest(s) remaining.')

        x, y = enter_player_move(previous_moves)
        # We must track all moves so that sonar devices can be updated.
        previous_moves.append([x, y])

        move_result = make_move(the_board, the_chests, x, y)
        if move_result == False:
            continue
        else:
            if move_result == 'You have found a sunken treasure chest!':
                # Update all sonar devices currently on the map.
                for x, y in previous_moves:
                    make_move(the_board, the_chests, x, y)

            draw_board(the_board)
            print(move_result)

        if len(the_chests) == 0:
            print(
                'You have found all the sunken treasure chests!  Congratulations and good game!')
            break

        sonar_devices -= 1

    if sonar_devices == 0:
        print(
            "We've run out of sonar devices!  Now we have to turn the ship around and head")
        print('for home with treasure chests still out there!  Game over')
        print('    The remaining chests were here:')
        for x, y in the_chests:
            print(f'    {x}, {y}')

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        sys.exit()
