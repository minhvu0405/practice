# def Solution(matrix):
# 	col = 0
# 	minCol = 0
# 	maxCol = len(matrix[0])-1
# 	row = 0
# 	minRow = 0
# 	maxRow = len(matrix)-1
# 	lenMatrix = len(matrix)*len(matrix[0])
# 	count = 1
# 	state = 0
# 	while count <= lenMatrix:
# 		matrix[row][col] = count
# 		count += 1
# 		if state == 0:
# 			col += 1
# 			if col == maxCol:
# 				state = 1
# 				minRow += 1
# 		elif state == 1:
# 			row += 1
# 			if row == maxRow:
# 				state = 2
# 				maxCol -= 1
# 		elif state == 2:
# 			col -= 1
# 			if col == minCol:
# 				state = 3
# 				maxRow -= 1
# 		else:
# 			row -= 1
# 			if row == minRow:
# 				state = 0
# 				minCol += 1
# 	return matrix

# n = 80
# matrix = [[0 for i in range(n)] for j in range(n)]
# new =  Solution(matrix)
# print new
def generateMatrix(A):
    col = row = 0
    minCol = minRow = 0
    matrix = [[0 for i in range(A)] for j in range(A)]
    maxCol = len(matrix[0])-1
    maxRow = len(matrix) - 1
    lenMatrix = len(matrix[0])*len(matrix)
    count = 1
    state = 0
    while count <= lenMatrix:
    	matrix[row][col] = count
    	count += 1
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
    			minCol -= 1
    return matrix
print generateMatrix(3)