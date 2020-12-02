import random

NUM_DIGITS = 3
MAX_GUESS = 10


def get_secret_num():
    """Returns a string of unique random digits that is NUM_DIGITS ong.

    Returns:
        string: unique random number
    """
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_num = ''

    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])

    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with the Pico, Fermi, & Bagels clues to the user.

    Args:
        guess (string): Users guess at the number generated
        secret_num (string): number user is trying to guess

    Returns:
        string: results of user's guess
    """
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)


def is_only_digits(num):
    """Returns True if num is a string of only digits.

    Args:
        num (string): User's guessed input

    Returns:
        bool: True if user inputed only numbers.  Otherwise false
    """
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print(f'I am thinking of a {NUM_DIGITS} digit number.  Try to guess what it is.')
print('The clues I give are...')
print('When I say:    That means:')
print('  Bagels       None of the digits is correct.')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')

while True:
    secret_num = get_secret_num()
    print(
        f'I have thought up a number.  You have {MAX_GUESS} guesses to get it.  Good luck!')

    guesses_taken = 1
    while guesses_taken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not is_only_digits(guess):
            print(f'Guess #{guesses_taken}')
            guess = input()

        print(get_clues(guess, secret_num))
        guesses_taken += 1

        if guess == secret_num:
            break
        if guesses_taken > MAX_GUESS:
            print(f'You ran out of guesses.  The answer was {secret_num}')

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
