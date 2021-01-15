#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:53:09 2021

@author: tonytang
"""

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('{:^3} | {:^3} | {:^3}'.format(board[1],board[2],board[3]))
    print('---------------')
    print('{:^3} | {:^3} | {:^3}'.format(board[4],board[5],board[6]))
    print('---------------')
    print('{:^3} | {:^3} | {:^3}'.format(board[7],board[8],board[9]))
    
    
def player_input():
    marker=' '
    
    while marker != 'O' and marker != 'X':
        marker=input('Player1 , choose O or X?').upper()
        
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    board[position]=marker
    
    
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))
    

import random

def choose_first():
    if random.randint(1,2)==1:
        return('player1')
    else:
        return('player2')
        
def space_check(board, position):
    return board[position]==' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def replay():
    choose = input('Play Again? Y or N').upper()
    return choose=='Y'


print('Welcome to Tic Tac Toe!')
while True:
    the_board=[' ']*10
    display_board(the_board)
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' first ')
    play_game=input('Ready to play, Y or N?').upper()
    if play_game=='Y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        if turn == 'player1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player1 Win!!')
                game_on = False
            else:
                if full_board_check(the_board):               
                    display_board(the_board)
                    print('Tie Game!!')
                    break
                else:
                    turn = 'player2'
                
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker ,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player2 Win!!')
                game_on = False
            else:           
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    break
                else:
                    turn = 'player1'
    if not replay():
        break
            
    
    
#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break