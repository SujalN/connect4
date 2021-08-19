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
    print(np.flipud(board))

def winning_move(board, piece):
    # check for horizontal win
    for col in range(COLS - 3):
        for row in range(ROWS):
            if board[row][col] == piece and \
                board[row][col + 1] == piece and \
                board[row][col + 2] == piece and \
                board[row][col + 3] == piece:
                    return True

    # check for vertical win
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            if board[row][col] == piece and \
                board[row + 1][col] == piece and \
                board[row + 2][col] == piece and \
                board[row + 3][col] == piece:
                    return True

    # check for positively sloped diagonal win
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            if board[row][col] == piece and \
                board[row + 1][col + 1] == piece and \
                board[row + 2][col + 2] == piece and \
                board[row + 3][col + 3] == piece:
                    return True

    # check for negatively sloped diagonal win
    for col in range(COLS - 3):
        for row in range(3, ROWS):
            if board[row][col] == piece and \
                board[row - 1][col + 1] == piece and \
                board[row - 2][col + 2] == piece and \
                board[row - 3][col + 3] == piece:
                    return True

board = create_board()
game_over = False
turn = True

while not game_over:
    if turn:
        col = int(input("Player 1, make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, P1_PIECE)
            if winning_move(board, P1_PIECE):
                print("Player 1 wins!")
                game_over = True
    else:
        col = int(input("Player 2, make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, P2_PIECE)
            if winning_move(board, P2_PIECE):
                print("Player 2 wins!")
                game_over = True
                 
    print_board(board)
    turn = not turn