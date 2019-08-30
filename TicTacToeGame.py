
#Creating a tic tac toe game in python
import random
#Drawing the board
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#Creating multiple blanks
board = [' '] * 10
#Testing the board function
#print(drawBoard(board))

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
# =============================================================================
#     The first element in the list is the player's
#     letter, the second is the computer's letter
# =============================================================================
    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
#This function returns True if the player wants t oplay again, otherwise it returns false
def playAgain():
    print('Do you want to play again? (yes/no)')
    return input().lower().startswith('y')
def makeMove(board, letter, move):
    board[move] = letter
#
def isWinner(b,l):
    return((b[7] == l and b[8] == l and b[9] == l) or
           (b[4] == l and b[5] == l and b[6] == l) or
           (b[1] == l and b[2] == l and b[3] == l) or
           (b[7] == l and b[4] == l and b[1] == l) or
           (b[8] == l and b[5] == l and b[2] == l) or
           (b[9] == l and b[6] == l and b[3] == l) or
           (b[7] == l and b[5] == l and b[3] == l) or
           (b[9] == l and b[5] == l and b[1] == l))
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return(dupeBoard)
#Return true if the passed move is free on the passed board
def isSpaceFree(board, move):
        return board[move] == ' '
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return(int(move))
def chooseRandomMoveFromList(board, moveList):
# =============================================================================
# Returns a valid move from teh passed list on the board
# Return non if there is no valid move
# =============================================================================
    possibleMoves =[]
    for i in moveList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return(random.choice(possibleMoves))
    else:
        return(None)
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
#Algorithm for AI: First check if we can win in the move 
    for i in range(1,10):
         copy = getBoardCopy(board)
         if isSpaceFree(copy,i):
             makeMove(copy, computerLetter, i)
             if isWinner(copy, computerLetter):
                 return(i)
#Check if the player could win on their next move and block them
    for i in range(1,10):
         copy = getBoardCopy(board)
         if isSpaceFree(copy,i):
             makeMove(copy, playerLetter, i)
         if isWinner(copy, playerLetter):
                return(i)
#Try to take one of the corners if they are free
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return(None)
#Try to take the center, if its free
    if isSpaceFree(board,5):
        return(5)
#Move to one of the sides
    return(chooseRandomMoveFromList(board, [2,4,6,8]))
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return(False)
    return(True)
        
print("Welcome to the Tic Tac Toe Game!") 
while True:
    theBoard=[' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The '+ turn + ' will go first.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            #players turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove =(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Congrats! You win!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('It%s a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            #Computers turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Damn! You lost to a computer!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
# =============================================================================
# if not playAgain():
#     break
# =============================================================================
