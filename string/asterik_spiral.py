def drawSpiral(n):
	length = n*(n+1)*0.5
	matrix = [[' ' for i in range(n)] for j in range(n)]
	maxCol = len(matrix[0]) - 1
	maxRow = len(matrix) - 1
	minRow = 0
	minCol = 1
	row = col = 0
	count = 0
	state = 0
	while count < length:
		matrix[row][col] = "*"
		count += 1
		if state == 0:
			col += 1
			if col == maxCol:
				state = 1
				minRow += 2
		elif state == 1:
			row += 1
			if row == maxRow:
				state = 2
				maxCol -= 2
		elif state == 2:
			col -= 1
			if col == minCol:
				state = 3
				maxRow -= 2
		else:
			row -= 1
			if row == minRow:
				state = 0
				minCol += 2
	return matrix
def printMatrix(matrix):
	for i in matrix:
		print i

if __name__ == '__main__':
	m = drawSpiral(6)
	printMatrix(m)

