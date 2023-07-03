import pygame
import sys
import time
import numpy as np
from board import Board
from pieces import Null, Piece
from checking import get_attacked_pos,find_kings, check_attacking_check

#initialize pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('NIC\'S CHESS')
clk = pygame.time.Clock()

#Define board size and square size
board_size = 512
square_size = board_size//8

#Define colors for the board
LIGHT_SQUARE = (238,232,170)
DARK_SQAURE = (0,128,128)
HIGHLIGHT = (100,100,100)

#Set font and font size for any text in the game
font = pygame.font.Font('freesansbold.ttf',20)

#Create game window
window = pygame.display.set_mode((board_size,board_size))

#Load in chess piece images from ./pieces (lookup table)
piece_pics = {'wR':pygame.image.load('pieces/wR.png'),
			  'wN':pygame.image.load('pieces/wN.png'),
			  'wB':pygame.image.load('pieces/wB.png'),
			  'wQ':pygame.image.load('pieces/wQ.png'),
			  'wK':pygame.image.load('pieces/wK.png'),
			  'wP':pygame.image.load('pieces/wP.png'),
			  'bR':pygame.image.load('pieces/bR.png'),
			  'bN':pygame.image.load('pieces/bN.png'),
			  'bB':pygame.image.load('pieces/bB.png'),
			  'bQ':pygame.image.load('pieces/bQ.png'),
			  'bK':pygame.image.load('pieces/bK.png'),
			  'bP':pygame.image.load('pieces/bP.png')
			  }

#Initialize Board object
b = Board()
print('Board Initialized.')
#Define function to draw the checkered pattern on the board
def draw_tiles():
	#Have to reverse the order of the rows since I want to
	#start from bottom left corner
	for row in reversed(range(8)):
		for col in range(8):
			x = col*square_size
			y = (7-row)*square_size

			if (row+col)%2 == 0:
				pygame.draw.rect(window, DARK_SQAURE,
					(x,y,square_size,square_size))
			elif (row+col)%2 !=0:
				pygame.draw.rect(window, LIGHT_SQUARE,
					(x,y,square_size,square_size))

def draw_pieces(b):
		for row in range(8):
			for col in range(8):
				if not b.board[row][col].is_empty:
					current_piece = piece_pics[b.board[row][col].color+
					b.board[row][col].name]
					x = col*square_size
					y = (7-row)*square_size
					window.blit(current_piece,(x,y))

def draw_board(board):
	draw_tiles(board)
	draw_pieces(board)

def highlight_moves(legal_moves):
    # Create a transparent surface for highlighting moves
		if legal_moves is not None:
			for move in legal_moves:
				x = move[1]*square_size + .5*square_size
				y = (7 - move[0])*square_size + .5*square_size
				pygame.draw.circle(window, HIGHLIGHT,(x,y),8)

def main():
	#Start running
	done = False
	turn = 'w'
	piece = Null(None,(0,0)) # initialize piece as empty piece
	selected_piece = piece
	selected_pos = []
	legal_moves = []
	print("Starting Game.\n")
	while not done:
		new_piece = False
		#Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				click_pos = pygame.mouse.get_pos()

				row = (board_size - click_pos[1])//square_size
				col = click_pos[0]//square_size
				pos = (row,col)

				piece = b.board[row][col]
				new_piece = True


		#Clear display
		window.fill((0,0,0))

		#Draw board and current piece positions
		draw_tiles()
		draw_pieces(b)

		#Highlight possible moves and get legal_moves when new piece selected
		if new_piece:
			if pos in legal_moves:
				b.move_piece(selected_pos,pos)
				turn = 'w' if turn == 'b' else 'b'
				legal_moves = []

				print(f"{selected_piece.color}{selected_piece.name}"
					f" moved to: {pos}")
			elif piece.color == turn:
				legal_moves = piece.get_legal_moves(board=b.board)[0]
			else:
				legal_moves = []

			selected_pos = pos
			selected_piece = piece 

			print(f"\nSelected piece : "
				f"{selected_piece.color}{selected_piece.name}")
			print(f"Can move to {legal_moves}")
			get_attacked_pos(board=b.board)
			print(find_kings(b.board))
			check_attacking_check(turn, b.board)
			
		highlight_moves(legal_moves)

		#Update the pygame window
		pygame.display.update()

		#Enfore 30 FPS
		clk.tick(30)

	#Close the window once the "x" is clicked on
	pygame.quit()
	sys.exit()

main()