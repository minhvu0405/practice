def Solution(matrix):
	for i in range(len(matrix)):
		for j in range(i,len(matrix)):
			print i,j
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp
	for i in range(n):
		print matrix[i]
	for i in matrix:
		i.reverse()
	return matrix
def Solution2(matrix):
	minCol = minRow = 0
	maxCol = len(matrix[0]) - 1
	maxRow = len(matrix) - 1
	lenMatrix = len(matrix[0])*len(matrix)
	state = 0
	count = 0
	row = col = 0
	while minCol < maxCol and minRow < maxRow:
		save = matrix[minRow+1][minCol]
		for i in range(minCol,maxCol+1):
			pre = matrix[minRow][i]
			matrix[minRow][i] = save
			save = pre
		minRow += 1
		
		for i in range(minRow,maxRow+1):
			pre = matrix[i][maxCol]
			matrix[i][maxCol] = save
			save = pre
		maxCol -= 1

		for i in range(maxCol,minCol-1,-1):
			pre = matrix[maxRow][i]
			matrix[maxRow][i] = save
			save = pre
		maxRow -= 1
		
		for i in range(maxRow,minRow-1,-1):
			pre = matrix[i][minCol]
			matrix[i][minCol] = save
			save = pre
		minCol += 1
	return matrix
n = 3
matrix = [[0 for i in range(n)] for j in range(n)]
count = 1
for i in range(n):
	for j in range(n):
		matrix[i][j] = count
		count += 1

for i in range(n):
	print matrix[i]
print
m = Solution(matrix)
print
for i in range(n):
	print m[i]