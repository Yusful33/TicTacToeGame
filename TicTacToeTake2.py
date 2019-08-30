# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:48:59 2019

@author: ycattaneo
"""

#Clears the board
#print('\n'*100)
#Creating a board
def display_board(b):
    print('\n'*100)
    print('   |   |')
    print(' ' + b[7] + ' | ' + b[8] + ' | ' + b[9])
    print('-----------')
    print(' ' + b[4] + ' | ' + b[5] + ' | ' + b[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + b[1] + ' | ' + b[2] + ' | ' + b[3])
#Testing out the above function
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)
#Assigns a marker of X or O 
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?')
    if marker  == 'X':
        return('X', 'O')
    else: 
        return('O', 'X')
#Testing above function
#player_input()

#Function to takes in the board list object (x,o) and
#desired position and assigns it to the board
def place_marker(b, l, position):
    b[position] = l
#Testing function
#place_marker(test_board, '$', 8)
#display_board(test_board)

#Function that takes in a board and a marker and then
#checks to see if that mark has won
def win_check(b,l):
    return((b[7] == l and b[8] == l and b[9] == l) or
           (b[4] == l and b[5] == l and b[6] == l) or
           (b[1] == l and b[2] == l and b[3] == l) or
           (b[7] == l and b[4] == l and b[1] == l) or
           (b[8] == l and b[5] == l and b[2] == l) or
           (b[9] == l and b[6] == l and b[3] == l) or
           (b[7] == l and b[5] == l and b[3] == l) or
           (b[9] == l and b[5] == l and b[1] == l))
#Testing
#win_check(test_board, 'O')

import random
#Function that uses a random module to randomly decide
#which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
#Checking if any spaces on the board are free
def space_check(b,position):
    return(b[position] == ' ')
#Checking if the board is full
def full_board_check(b):
    for i in range(1,10):
        if space_check(b, i):
            return(False)
    return(True)
#Asks for players ext position and then checks if that 
#position is free
def player_choice(b):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(b,position):
        position = int(input('Choose your next position (1-9)'))
    return(position)
#Asks if they want to play again
def replay():
    return(input('Do you want to play again? Enter Yes or No: ').lower().startswith('y'))
    
    
####RUN Below Code to Play###########

#Using functions above to play the game
print('Welcome to Tic Tac Toe!')
while True:
    #Reset the board
    theBoard = [' '] *10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No. ')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            #Player1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            #Player2's Turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
                











