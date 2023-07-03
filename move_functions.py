def check_left_diagonal(pos,color,board):
	'''
	Return legal moves on left (negative slope) diagonal
	'''
	legal_moves = []
	row, col = pos

	up_left = []
	down_right = [] 

	for i in range(1,8):
		if row+i <= 7 and col-i >= 0: 
			up_left.append((row+i,col-i))
		if row-i >= 0 and col+i <= 7:
			down_right.append((row-i,col+i))

	#Check moves up and left 
	for pos in up_left:
		if board[pos[0]][pos[1]].is_empty:
			legal_moves.append(pos)
		elif board[pos[0]][pos[1]].color != color:
			legal_moves.append(pos)
			break
		else:
			break

	#Check moves down and right
	for pos in down_right:
		if board[pos[0]][pos[1]].is_empty:
			legal_moves.append(pos)
		elif board[pos[0]][pos[1]].color != color:
			legal_moves.append(pos)
			break
		else:
			break

	return legal_moves

def check_right_diagonal(pos,color,board):
	'''
	Return legal moves on right (positive slope) diagonal
	'''
	legal_moves = []
	row, col = pos

	up_right = []
	down_left = []

	for i in range(1,8):
		if row+i <= 7 and col+i <= 7:
			up_right.append((row+i,col+i))
		if row-i >= 0 and col-i >= 0:
			down_left.append((row-i,col-i))

	#Check moves up and right
	for pos in up_right:
		if board[pos[0]][pos[1]].is_empty:
			legal_moves.append(pos)
		elif board[pos[0]][pos[1]].color != color:
			legal_moves.append(pos)
			break
		else:
			break

	#Check moves down and left
	for pos in down_left:
		if board[pos[0]][pos[1]].is_empty:
			legal_moves.append(pos)
		elif board[pos[0]][pos[1]].color != color:
			legal_moves.append(pos)
			break
		else:
			break

	return legal_moves

def check_row(pos,color,board):
	'''
	Return legal moves on row
	'''
	legal_moves = []
	row, col = pos

	whole_row = [(row,x) for x in range(8)]

	#Check moves left
	if col != 0:
			for pos in whole_row[col-1::-1]:
				if board[pos[0]][pos[1]].is_empty:
					legal_moves.append(pos)
				elif board[pos[0]][pos[1]].color != color:
					legal_moves.append(pos)
					break
				else:
					break

		#Check moves right
	if col != 7:
		for pos in whole_row[col+1:]:
			if board[pos[0]][pos[1]].is_empty:
				legal_moves.append(pos)
			elif board[pos[0]][pos[1]].color != color:
				legal_moves.append(pos)
				break
			else:
				break

	return legal_moves

def check_col(pos,color,board):
	'''
	Return legal moves on column
	'''
	legal_moves = []
	row, col = pos

	whole_col = [(x,col) for x in range(8)]

	#Check moves up
	if row != 7:
		for pos in whole_col[row+1:]:
			if board[pos[0]][pos[1]].is_empty:
				legal_moves.append(pos)
			elif board[pos[0]][pos[1]].color != color:
				legal_moves.append(pos)
				break
			else:
				break

		#Check moves down
	if row != 0:
		for pos in whole_col[row-1::-1]:
			if board[pos[0]][pos[1]].is_empty:
				legal_moves.append(pos)
			elif board[pos[0]][pos[1]].color != color:
				legal_moves.append(pos)
				break
			else:
				break

	return legal_moves