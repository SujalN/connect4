import numpy as np

ROWS, COLS, P1_PIECE, P2_PIECE = 6, 7, 1, 2

def create_board():
    return np.zeros((ROWS, COLS))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROWS - 1][col] == 0

def get_next_open_row(board, col):
    for row in range(ROWS):
        if board[row][col] == 0:
            return row

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    pass

board = create_board()
game_over = False
turn = True

while not game_over:
    if turn:
        col = int(input("Player 1, make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, P1_PIECE)
    else:
        col = int(input("Player 2, make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, P2_PIECE)
    print_board(board)
    turn = not turn