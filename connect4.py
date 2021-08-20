import numpy as np
import pygame as pg
import sys
import math

ROWS, COLS, P1_PIECE, P2_PIECE, SQUARESIZE = 6, 7, 1, 2, 100
BLUE, BLACK, RED, YELLOW = (0, 0, 225), (0, 0, 0), (225, 0, 0), (225, 225, 0)
RADIUS, HEIGHT = int(SQUARESIZE / 2 - 5), (ROWS + 1) * SQUARESIZE

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

    # check for positively-sloped diagonal win
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            if board[row][col] == piece and \
                board[row + 1][col + 1] == piece and \
                board[row + 2][col + 2] == piece and \
                board[row + 3][col + 3] == piece:
                    return True

    # check for negatively-sloped diagonal win
    for col in range(COLS - 3):
        for row in range(3, ROWS):
            if board[row][col] == piece and \
                board[row - 1][col + 1] == piece and \
                board[row - 2][col + 2] == piece and \
                board[row - 3][col + 3] == piece:
                    return True

def draw_board(board):
    # set up empty board
    for col in range(COLS):
        for row in range(ROWS):
            pg.draw.rect(screen, BLUE, (col*SQUARESIZE, row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pos = (int(col*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2))
            pg.draw.circle(screen, BLACK, pos, RADIUS)
    
    # add pieces
    for col in range(COLS):
        for row in range(ROWS):
            if board[row][col] == 1:
                pos = (int(col*SQUARESIZE+SQUARESIZE/2), HEIGHT - int(row*SQUARESIZE+SQUARESIZE/2))
                pg.draw.circle(screen, RED, pos, RADIUS)
            elif board[row][col] == 2:
                pos = (int(col*SQUARESIZE+SQUARESIZE/2), HEIGHT - int(row*SQUARESIZE+SQUARESIZE/2))
                pg.draw.circle(screen, YELLOW, pos, RADIUS)
    pg.display.update()

board = create_board()
game_over = False
turn = True
# initalize pygame screen
pg.init()
size = (COLS * SQUARESIZE, (ROWS + 1) * SQUARESIZE)
screen = pg.display.set_mode()
draw_board(board)
pg.display.update()

while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            # let Player 1 play their turn
            if turn:
                col = int(math.floor(event.pos[0] / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, P1_PIECE)
                    if winning_move(board, P1_PIECE):
                        print("Player 1 wins!")
                        game_over = True
            
            # let Player 2 play their turn
            else:
                col = int(math.floor(event.pos[0] / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, P2_PIECE)
                    if winning_move(board, P2_PIECE):
                        print("Player 2 wins!")
                        game_over = True

    print_board(board)
    draw_board(board)
    turn = not turn