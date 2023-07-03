from pieces import Piece, Knight, Rook, Bishop, Pawn, King, Queen, Null
import numpy as np

class Board():
	def __init__(self):
		self.board = self.initialize_board()

	def initialize_board(self):
		'''
		Returns board in starting position (white on bottom)
		'''
		board = np.full((8,8),None)
		board[0][0] = Rook('w',(0,0))
		board[0][1] = Knight('w',(0,1))
		board[0][2] = Bishop('w',(0,2))
		board[0][3] = Queen('w',(0,3))
		board[0][4] = King('w',(0,4))
		board[0][5] = Bishop('w',(0,5))
		board[0][6] = Knight('w',(0,6))
		board[0][7] = Rook('w',(0,7))

		for i in range(8):
			board[1][i] = Pawn('w',(1,i))
			for j in range(2,6):
				board[6][i] = Pawn('b',(6,i))
				board[j][i] = Null('empty', (j,i))


		board[7][0] = Rook('b',(7,0))
		board[7][1] = Knight('b',(7,1))
		board[7][2] = Bishop('b',(7,2))
		board[7][3] = Queen('b',(7,3))
		board[7][4] = King('b',(7,4))
		board[7][5] = Bishop('b',(7,5))
		board[7][6] = Knight('b',(7,6))
		board[7][7] = Rook('b',(7,7))

		return board

	def move_piece(self,currentpos,newpos):
		'''
		Swaps piece in board when moved. Only when moving to a Null Piece.
		'''
		curr_piece = self.board[currentpos[0]][currentpos[1]]
		other_piece = self.board[newpos[0]][newpos[1]]

		#If takes, replace taken piece with Null piece
		if not other_piece.is_empty:
			other_piece = Null('empty',(newpos[0],newpos[1]))

		#Change position on board array
		self.board[currentpos[0]][currentpos[1]] = other_piece
		self.board[newpos[0]][newpos[1]] = curr_piece

		#Need to update the position of the piece objects as well
		self.board[currentpos[0]][currentpos[1]].move(currentpos)
		self.board[newpos[0]][newpos[1]].move(newpos)

