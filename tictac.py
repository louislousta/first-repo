# a tic tac toe game for two players 
import sys,random

def new_board():
    board = [[None,None,None],[None,None,None],[None,None,None]]
    return board

def render_board(board):
    for i in range(3):
        print('-------------------------')
        for j in range(3):
            print('|', board[i][j], '|', end = '')
        print()

def get_move(): #takes input in form tl/tm/etc and returns list index
    move = input()
    move_index = list
    match move:
        case 'tl':
            move_index = [0,0] 
        case 'tm':
            move_index = [0,1]
        case 'tr': 
            move_index = [0,2]
        case 'ml':
            move_index = [1,0]
        case 'mm':
            move_index = [1,1]
        case 'mr': 
            move_index = [1,2]
        case 'bl':
            move_index = [2,0]
        case 'bm': 
            move_index = [2,1]
        case 'br': 
            move_index = [2,2]
        case 'q','quit':
            sys.exit(0)
        case _:
            raise ValueError
    return move_index

def update_board(board,move,player):
    new_board = board
    if board[move[0]][move[1]] == None:
        new_board[move[0]][move[1]] = player
    else: 
        raise ValueError
    return new_board
   
def is_winner(board):
    line_1 = [board[0][0],board[0][1],board[0][2]]
    line_2 = [board[1][0],board[1][1],board[1][2]]
    line_3 = [board[2][0],board[2][1],board[2][2]]
    line_4 = [board[0][0],board[1][0],board[2][0]]
    line_5 = [board[0][1],board[1][1],board[2][1]]
    line_6 = [board[0][2],board[1][2],board[2][2]]
    line_7 = [board[0][0],board[1][1],board[2][2]]
    line_8 = [board[0][2],board[1][1],board[2][0]]
    lines = [line_1,line_2,line_3,line_4,line_5,line_6,line_7,line_8]
    for line in lines:
        if line[0] == line[1] and line[1] == line[2]:
            return line[0]
    
init_board = new_board()        
player = 'X'
while True:
    
    print(player, ': Your turn, make a move')
    try:
        move = get_move()
    except: 
        print("Not a valid move! Try 'tl' for top left, 'bm' for bottom middle, 'mm' for middle middle etc..")
        continue
    try:
        next_board = update_board(init_board,move,player)
    except:
        print('Sorry, somebody already made that move! Try again.')
        continue
    
    render_board(next_board)
    winner = is_winner(next_board)
    if winner == 'X' or winner == 'O':
        break
    init_board = next_board
    if player != 'O':
        player = 'O'
    else: player = 'X'

print('Congratulations {w}! You win!'.format(w = winner))