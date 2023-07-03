from pieces import King

def check_defending_check(color,board):
	'''
	See if proposed move puts own king in check
	'''
	return

def check_attacking_check(color,board):
	'''
	See if last move puts opponent into check
	'''
	attacking_pos = get_attacked_pos(board)
	king_pos = find_kings(board)

	if king_pos[color] in attacking_pos:
		print(f"{color} is checking")
	return

def check_defending_mate(color,board):
	return 

def check_attacking_mate(color,board):
	return

def check_check(color,board):
	return

def check_mate(color,board):
	return

def get_attacked_pos(board):
	'''
	Return all attacked positions for white and black in a dictionary
	'''
	attacking_pos = {'w': [],'b': []}

	for row in board:
		for piece in row:
			#print(piece)
			if piece.color == 'w':
				attacking_pos['w'].append(piece.get_legal_moves(board)[1])
			elif piece.color == 'b':
				attacking_pos['b'].append(piece.get_legal_moves(board)[1])
			else:
				continue
	print(attacking_pos['w'])

	return attacking_pos

def find_kings(board):
	'''
	Return positions of both kings in a dictionary
	'''
	king_pos = {'w':(),'b':()}
	for row in range(8):
		for col in range(8):
			if isinstance(board[row][col], King):
				if board[row][col].color == 'w':
					king_pos['w'] = board[row][col].pos
				elif board[row][col].color == 'b':
					king_pos['b'] = board[row][col].pos

	return king_pos

