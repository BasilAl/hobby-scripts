# This is the Guess the number game
import random

guessesTaken = 0

print('Hello! What is your name?')
myname = input()

number = random.randint(1,20)
print('Well, ' +myname+ ', I am thinking of a number between 1 and 20.')

while guessesTaken <6:
    print('Take a guess!')
    guess=input()
    guess=int(guess)

    guessesTaken=guessesTaken +1

    if guess<number:
        print('too low')

    if guess>number:
        print('too high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' +myname + '! you guessed my number in ' +guessesTaken +' guesses')

if guess != number:
    number=str(number)
    print('Nope, the number was ' +number)
