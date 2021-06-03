import random
import os

def drawBoard(board):
    #draws the board that it's given as a list of 10 strings
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def inputPlayerLetter():
    #lets the player type which leatter they want to be
    #returns a list with the players letter as the first item and the computers as the sedcond
    letter=''
    while not(letter=='X' or letter=='O'):
        print('Do you want to be X or O?')
        letter=input().upper()
    if letter=='X':
        return ['X', 'O']
    else:
        return ['O','X']

def whoGoesFirst():
    #randomly choose who goes first
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'



def makeMove(board,letter,move):
    board[move]=letter

def isWinner(bo,le):
    #given board and player's letter it returns true if the player won,
    return((bo[7]==le and bo[8]==le and bo[9]==le) or
           (bo[4]==le and bo[5]==le and bo[6]==le) or
           (bo[1]==le and bo[2]==le and bo[3]==le) or
           (bo[1]==le and bo[5]==le and bo[9]==le) or
           (bo[7]==le and bo[5]==le and bo[3]==le) or
           (bo[1]==le and bo[4]==le and bo[7]==le) or
           (bo[8]==le and bo[5]==le and bo[2]==le) or
           (bo[9]==le and bo[6]==le and bo[3]==le))

def getBoardCopy(board):
    boardCopy=[]
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board,move):
    #true if passed move is free on board
    return board[move]==' '

def getPlayerMove(board):
    #let the player make their move
    move=' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move=input()
    return int(move)

def chooseRandomMoveFromList(board,movesList):
    #returns a valid move from the passed list on the passed board
    #or none if there's no valid move
    #we could also make it return with a freddo sketo, but we didn't
    #cause we're mean like that
    possibleMoves=[]
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #given a board and the computer's letter, determine wher to move
    #and return that move
    if computerLetter=='X':
        playerLetter='O'
    else:
            playerLetter='X'
    #here we make some ai using the latest and most advanced algorithms
    #that deepmind could come up with by initially checking if the ai wins
    for i in range(1,10):
        boardCopy=getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    #or checking if the player is gud and can win on the next move
    for i in range(1,10):
        boardCopy=getBoardCopy(board)
        if isSpaceFree(boardCopy,i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    #if player not gud enough, take a corner cause he won't think to corner u
    move=chooseRandomMoveFromList(board,[1,3,7,9])
    if move!=None:
        return move

    #if plya in corner, go 2 center and punch him in the face
    if isSpaceFree(board,5):
        return 5
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    #oti leei to onoma
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

print('Welcome to Tic-Tac-Toe!')

while True:
    #reset the board
    theBoard=[' ']*10
    playerLetter, computerLetter=inputPlayerLetter()
    turn=whoGoesFirst()
    print('The '+turn+' will go first.')
    gameIsPlaying=True

    while gameIsPlaying:
        if turn=='player':
            #playa's turn
            drawBoard(theBoard)
            move=getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter,move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You are gud!')
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Hurrah, you are as gud as a stupid computer!')
                    break
                else:
                    turn='computer'

        else:
            #computers turn
            move=getComputerMove(theBoard,computerLetter)
            makeMove(theBoard,computerLetter,move)

            if isWinner(theBoard,computerLetter):
                drawBoard(theBoard)
                print('The computer is so gud, and you are a nubkek')
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('to paixnidi einai gravata')
                    break
                else:
                    turn='player'
    print('Do you want to play again?(this is a binary question there is only one correct answer)')
    if not input().lower().startswith('y'):
        break
