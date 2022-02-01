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
        case _:
            raise ValueError
    return move_index

def update_board(board,move,player):
    if board[move[0]][move[1]] == None:
        board[move[0]][move[1]] = player
    else: 
        raise ValueError
    return board

def win_con(board): #deal with this later
    pass
        
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
    if player != 'O':
        player = 'O'
    else: player = 'X'