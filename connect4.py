import numpy as np
import pygame as pg
import sys
import math

BLUE, BLACK, RED, YELLOW = (0, 0, 255), (0, 0, 0), (255, 0, 0), (255, 255, 0)
ROWS, COLS, SQUARESIZE = 6, 7, 100
WIDTH, HEIGHT = COLS * SQUARESIZE, (ROWS+1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)

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
	# Check horizontal locations for win
	for col in range(COLS - 3):
		for row in range(ROWS):
			if board[row][col] == piece and \
            board[row][col + 1] == piece and \
            board[row][col + 2] == piece and \
            board[row][col + 3] == piece:
				return True

	# Check vertical locations for win
	for col in range(COLS):
		for row in range(ROWS - 3):
			if board[row][col] == piece and \
            board[row + 1][col] == piece and \
            board[row + 2][col] == piece and \
            board[row + 3][col] == piece:
				return True

	# Check positively sloped diaganols
	for col in range(COLS - 3):
		for row in range(ROWS - 3):
			if board[row][col] == piece and \
            board[row + 1][col + 1] == piece and \
            board[row + 2][col + 2] == piece and \
            board[row + 3][col + 3] == piece:
				return True

	# Check negatively sloped diaganols
	for col in range(COLS - 3):
		for row in range(3, ROWS):
			if board[row][col] == piece and \
            board[row - 1][col + 1] == piece and \
            board[row - 2][col + 2] == piece and \
            board[row - 3][col + 3] == piece:
				return True

def draw_board(board):
	for col in range(COLS):
		for row in range(ROWS):
			pg.draw.rect(screen, BLUE, (col * SQUARESIZE, row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pg.draw.circle(screen, BLACK, (int(col * SQUARESIZE + SQUARESIZE / 2), int(row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
	for col in range(COLS):
		for row in range(ROWS):		
			if board[row][col] == 1:
				pg.draw.circle(screen, RED, (int(col * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(row * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
			elif board[row][col] == 2: 
				pg.draw.circle(screen, YELLOW, (int(col * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(row * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
	pg.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0
pg.init()
RADIUS = int(SQUARESIZE / 2 - 5)
screen = pg.display.set_mode(SIZE)
draw_board(board)
pg.display.update()
myfont = pg.font.SysFont("monospace", 75)
while not game_over:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		if event.type == pg.MOUSEMOTION:
			pg.draw.rect(screen, BLACK, (0,0, WIDTH, SQUARESIZE))
			x_pos = event.pos[0]
			if turn == 0:
				pg.draw.circle(screen, RED, (x_pos, int(SQUARESIZE / 2)), RADIUS)
			else: 
				pg.draw.circle(screen, YELLOW, (x_pos, int(SQUARESIZE / 2)), RADIUS)
		pg.display.update()
		if event.type == pg.MOUSEBUTTONDOWN:
			pg.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
			# Ask for Player 1 Input
			if turn == 0:
				x_pos = event.pos[0]
				col = int(math.floor(x_pos / SQUARESIZE))
				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 1)
					if winning_move(board, 1):
						screen.blit(myfont.render("Player 1 wins!", 1, RED), (40, 10))
						game_over = True

			# # Ask for Player 2 Input
			else:				
				x_pos = event.pos[0]
				col = int(math.floor(x_pos / SQUARESIZE))
				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 2)
					if winning_move(board, 2):
						screen.blit(myfont.render("Player 2 wins!", 1, YELLOW), (40, 10))
						game_over = True

			print_board(board)
			draw_board(board)
			turn += 1
			turn = turn % 2
			if game_over:
				pg.time.wait(3000)