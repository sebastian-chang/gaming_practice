import random
import drawings

words = {
    'animals': 'ant baboon badget bat bear beaver camel cat calm cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeion python rabbit ram rat raven rhinio salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
    'colors': 'red orange yellow green blue indigo violet white black brown'.split(),
    'shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon spetagon octagon'.split(),
    'fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
    }


def get_random_word(word_dict):
    """This function returns a random string from the passed list of strings

    Args:
        word_dict (diction): a dictionary of a list of words

    Returns:
        [string]: random string from the list of strings passed into function
    """
    # Randomly select a catagory
    word_key = random.choice(list(word_dict))
    # Randomly select a word from selected category
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return (word_dict[word_key][word_index], word_key)


def display_board(missed_letters, correct_letters, secret_word):
    print(drawings.HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
      # Replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
      # Show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    """This function makes sure the player entered a single letter and not something else.

    Args:
        already_guessed ([type]): [description]

    Returns:
        string: The letter the user inputted as a guess.
    """
    while True:
        print('Guess a letter:')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter.  Choose again:')
        elif guess not in 'abcdefghijklmonpqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def play_again():
    """This fucntion returns True if players wants to play again.  Otherwise false

    Returns:
        bool: Users response to wanting to play another game.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
difficulty = 'X'
while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()

if difficulty == 'M':
    del drawings.HANGMAN_PICS[8]
    del drawings.HANGMAN_PICS[7]
if difficulty == 'H':
    del drawings.HANGMAN_PICS[8]
    del drawings.HANGMAN_PICS[7]
    del drawings.HANGMAN_PICS[5]
    del drawings.HANGMAN_PICS[3]

missed_letters = ''
correct_letters = ''
secret_word, secret_set = get_random_word(words)
game_is_done = False

while True:
    print(f'The secret word is in the set: {secret_set}')
    display_board(missed_letters, correct_letters, secret_word)

    # Let the player enter a letter.
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        # Check if the player has won.
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f'Yes! The secret word is {secret_word}!  You have won!')
            game_is_done = True

    else:
        missed_letters = missed_letters + guess

        # Check if the player has lost.
        if len(missed_letters) == len(drawings.HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!')
            print(
                f'After {len(missed_letters)} missed guesses and {len(correct_letters)} correct guesses the word was {secret_word}')
            game_is_done = True

    # Ask if the player if they want to play again (but only if the game is done)
    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break
