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

