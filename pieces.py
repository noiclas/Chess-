from move_functions import check_left_diagonal, check_right_diagonal,\
						   check_row, check_col

class Piece():
	def __init__(self, color ,pos):
		self.color = color
		self.pos = pos
		self.is_empty = False
		self.has_moved = False

	def move(self,newpos):
		self.pos = newpos
		self.has_moved = True


class Pawn(Piece):
	def __init__(self,color,pos):
		super().__init__(color, pos)
		self.name = 'P'
		self.has_moved = False

	def get_legal_moves(self,board):
		'''
		Returns a list of legal moves given the current board configuration.
		'''
		legal_moves = []
		attacking_pos = []
		direction = 1 if self.color == 'w' else -1
		row,col = self.pos

		#check if pawn can move forward by 1 
		if board[row+direction][col].is_empty:
			legal_moves.append((row+direction,col))

			#check if pawn can move forward by 2
			if not self.has_moved:
				if board[row+2*direction][col].is_empty:
					legal_moves.append((row+2*direction,col))

		#check if pawn can take diagonally
		if col != 0:
			diag_left = board[row+direction][col-1]
			attacking_pos.append((row+direction,col-1))
			if not diag_left.is_empty and diag_left.color != self.color:
				legal_moves.append((row+direction,col-1))
		if col !=7:
			diag_right = board[row+direction][col+1]
			attacking_pos.append((row+direction,col+1))
			if not diag_right.is_empty and diag_right.color != self.color:
				legal_moves.append((row+direction,col+1))

		#EN PASSANT FOR LATER

		return legal_moves, attacking_pos


class Knight(Piece):
	def __init__(self,color,pos):
		super().__init__ (color, pos)
		self.name = 'N'

	def get_legal_moves(self,board):
		'''
		Returns a list of legal moves given the current board configuration.
		'''

		legal_moves = []
		row,col = self.pos

		#Get all L-moves possible (ignoring board boundary)
		poss_moves = []
		for i in [-2,2]:
			for j in [-1,1]:
				poss_moves.append((row+i,col+j))
				poss_moves.append((row+j,col+i))

		#Get rid of moves that are outside the board
		poss_moves = [pos for pos in poss_moves if 
						0<=pos[0]<=7 and 0<=pos[1]<=7]

		#Get rid of moves where same color piece is in the position
		for pos in poss_moves:
			if board[pos[0]][pos[1]].color != self.color:
				legal_moves.append(pos)

		attacking_pos = legal_moves

		return legal_moves, attacking_pos
		
	def move(self,newpos):
		self.pos = newpos

class Rook(Piece):
	def __init__(self,color,pos):
		super().__init__ (color, pos)
		self.name = 'R'
		self.has_moved = False

	def get_legal_moves(self,board):
		'''
		Returns a list of legal moves given the current board configuration.
		'''

		row_moves = check_row(self.pos,self.color,board)
		col_moves = check_col(self.pos,self.color,board)

		legal_moves = row_moves + col_moves
		attacking_pos = legal_moves
		#CASTLING FOR LATER

		return legal_moves, attacking_pos


class Bishop(Piece):
	def __init__(self, color, pos):
		super().__init__(color,pos)
		self.name = 'B'

	def get_legal_moves(self,board):
		'''
		Returns a list of legal moves given the current board configuration.
		'''

		right_diag_moves = check_right_diagonal(self.pos,self.color,board)
		left_diag_moves = check_left_diagonal(self.pos,self.color,board)

		legal_moves = right_diag_moves + left_diag_moves
		attacking_pos = legal_moves

		return legal_moves, attacking_pos


class Queen(Piece):
	def __init__(self, color, pos):
		super().__init__(color, pos)
		self.name = 'Q'

	def get_legal_moves(self,board):
		'''
		Returns a list of legal moves given the current board configuration.
		'''
		row_moves = check_row(self.pos,self.color,board)
		col_moves = check_col(self.pos,self.color,board)
		right_diag_moves = check_right_diagonal(self.pos,self.color,board)
		left_diag_moves = check_left_diagonal(self.pos,self.color,board)

		legal_moves = row_moves + col_moves + right_diag_moves +\
					  left_diag_moves
		attacking_pos = legal_moves

		return legal_moves, attacking_pos		

class King(Piece):
	def __init__(self,color,pos):
		super().__init__(color,pos)
		self.name = 'K'
		self.has_moved = False

	def get_legal_moves(self,board):
		'''
		Returns a list of legal moves given the current board configuration.
		'''
		legal_moves = []
		row,col = self.pos

		poss_moves = []

		for x in [-1,0,1]:
			for y in [-1,0,1]:
				if x == 0 and y ==0:
					continue
				elif row+x > 7 or row+x < 0 or col+y > 7 or col+y < 0:
					continue
				else:
					poss_moves.append((row+x,col+y))

		for pos in poss_moves:
			if board[pos[0]][pos[1]].is_empty or \
			board[pos[0]][pos[1]].color != self.color:
				legal_moves.append(pos)
			else:
				continue

		attacking_pos = legal_moves

		return legal_moves,attacking_pos
		

class Null(Piece):
	def __init__(self,color,pos):
		super().__init__(color,pos)
		self.is_empty = True
		self.name = ' piece'

	def get_legal_moves(self,board):
		return [],[]
