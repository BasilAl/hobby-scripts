import random
import subprocess as sp
import os
HANGMAN_PICS=['''
   +---+
   0   |
       |
       |
      ===''','''
   +---+
   0   |
       |
       |
      ===''','''
   +---+
   0   |
   |   |
       |
      ===''','''
   +---+
   0   |
  /|   |
       |
      ===''','''
   +---+
   0   |
  /|\  |
       |
      ===''','''
   +---+
   0   |
  /|\  |
  /    |
      ===''','''
   +---+
   0   |
  /|\  |
  / \  |
      ===''']

words='ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck aegle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex= random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters,SecretWord):
    os.system('cls' if os.name == 'nt' else 'clear')#Clears screen
    print('H A N G M A N')
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks='_'*len(secretWord)

    for i in range(len(secretWord)):#replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks= blanks[:i]+secretWord[i]+blanks[i+1:]

    for letter in blanks:#show the secret word with spaces in between each letter.
        print(letter, end='')
def getGuess(alreadyGuessed):
    #returns the letter the player entered. this function makes sure the player enterd a single letter and not something else.
        while True:
            print('\nGuess a letter.')
            guess=input()
            guess=guess.lower()
            if len(guess)!=1:
                print('PLease enter a single letter.')
            elif guess in alreadyGuessed:
                print('You have already guessed that leter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter an letter(of the English alphabet)')
            else:
                return guess

def playAgain():    
    #this function returns true if the player wants to play again otherwise it returns false
    print('Do you want to play again? [(y)es or (n)o]')
    return input().lower().startswith('y')


missedLetters=''
correctLetters=''
secretWord=getRandomWord(words)
gameIsDone=False

while True:
    displayBoard(missedLetters,correctLetters,secretWord)

    #let the player enter a letter.
    guess=getGuess(missedLetters+correctLetters)

    if guess in secretWord:
        correctLetters=correctLetters+guess

         #check if the player has won
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        if foundAllLetters:
            print('Yes! the secret word is "'+secretWord+'"! You have won!')
            gameIsDone=True

    else:
        missedLetters = missedLetters + guess

        #Check if player has guessed too many times and lost.
        if len(missedLetters)==len(HANGMAN_PICS)-1:       
            displayBoard(missedLetters,correctLetters,secretWord)
            print('You have run out of guesses!\nAfter '+str(len(missedLetters))+' missed guesses and '+str(len(correctLetters))+' correct guesses, the word was "'+secretWord+'"')
            gameIsDone=True

        #ask the player if they want to play again if the game is done
        if gameIsDone:
            if playAgain():
                missedLetters=''
                correctLetters=''
                gameIsDone=False
                secretWord=getRandomWord(words)
            else:
                break
            
