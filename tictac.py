# a tic tac toe game for two players 

def new_board():
    board = [[None,None,None],[None,None,None],[None,None,None]]
    return board

def render_board(board):
    for i in range(3):
        print('-------------------------')
        for j in range(3):
            print('|', board[i][j], '|', end = '')
        print()

init_board = new_board()
render_board(init_board)

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
    return move_index

while(True):
    move = get_move()
    print(move)