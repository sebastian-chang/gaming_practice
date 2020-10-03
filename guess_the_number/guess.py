# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print (f'Well, {myName}, I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number: 
    print(f'Good job, {myName}! You guessed my number in {guessesTaken} guesses!')

if guess != number:
    print(f'Nope. the number I was thinking of was {number}')
