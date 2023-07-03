import numpy as np

cells = np.random.randint(2,size=(8,8))

def update_random_cell(cells):
	rand_pos = np.random.randint(8,size=2)
	
	row, col = rand_pos

	neighbors = []

	if row != 0:
		#down
		neighbors.append(cells[row-1][col])
	if row != 7:
		#up
		neighbors.append(cells[row+1][col])
	if col != 0:
		#left
		neighbors.append(cells[row][col-1])
	if col != 7:
		#right
		neighbors.append(cells[row][col-1])

	for cell in neigbors:
		#Determine 

	return rand_pos, cell_val

pos, val = update_random_cell(cells)

cells[pos[0]][pos[1]] = val