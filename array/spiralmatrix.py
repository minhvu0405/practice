def solution(m):
	result = []
	maxcol = 5
	maxrow = 6
	col = 0
	row = 0
	while row < maxrow and col < maxcol:
		for i in range(col,maxcol):
			result.append(m[row][i])
		row += 1
		for i in range(row,maxrow,1):
			result.append(m[i][maxcol-1])
		maxcol -= 1
		if col < maxcol:
			for i in range(maxcol-1,col-1,-1):
				result.append(m[maxrow-1][i])
			maxrow -= 1
		if row < maxrow:
			for i in range(maxrow-1,row-1,-1):
				result.append(m[i][col])
			col += 1
	return result
def solution2(matrix):
	result = []
	if len(matrix) == 0:
		return result
	col = 0
	row = 0
	minCol = 0
	maxCol = len(matrix[0]) - 1 
	minRow = 0
	maxRow = len(matrix) - 1
	state = 0
	lenMatrix = len(matrix)*len(matrix[0])
	while len(result) < lenMatrix:
		result.append(matrix[row][col])
		if state == 0:
			col += 1
			if col == maxCol:
				state = 1
				minRow += 1
		elif state == 1:
			row += 1
			if row == maxRow:
				state = 2
				maxCol -= 1
		elif state == 2:
			col -= 1
			if col == minCol:
				state = 3
				maxRow -= 1
		else:
			row -= 1
			if row == minRow:
				state = 0
				minCol += 1
	return result
n = 3
m = [[0 for i in range(3)] for j in range(3)]
count = 1
for i in range(3):
	for j in range(3):
		m[i][j] = count
		count += 1
for i in range(3):
		print m[i]
print
print solution2(m)