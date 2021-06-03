import random
import time
import sys

def read(string):
    i=0
    while i<len(string):
        print(string[i],end='')
        time.sleep(0.05)
        if string[i]=='.':
            time.sleep(0.5)
        sys.stdout.flush()
        i=i+1
    print('')

def displayIntro():
    intro='''You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.'''
    i=0
    read(intro)


def chooseCave():
    cave=''
    i=0

    question='Which cave will you go into? (1 or 2)'
    j=0
    print('')
    read(question)
    print('')
    while cave != '1' and cave != '2' and i<=10:
        cave = input()
        i=i+1

    return cave

def checkCave(chosenCave):
    approach='You approach the cave...'
    j=0
    read(approach)
    print()
    spooky='It\'s dark and spooky...'
    j=0
    read(spooky)
    time.sleep(1)
    print()
    print('\nA large dragon jumps out in front of you! He opens his jaw and...')
    time.sleep(1.5)

    friendlyCave=random.randint(1,2)
    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain='yes'
while playAgain=='yes' or playAgain== 'y':
    displayIntro()
    caveNumber=chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()

print('Party pooper!')
