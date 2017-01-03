def Solution(matrix):
	result = []
	if len(matrix) != len(matrix[0]):
		return result
	count = 0
	maxCol = len(matrix[0]) - 1
	maxRow = len(matrix) - 1
	state = 0
	col = row = 0
	lenBound = len(matrix[0]) + len(matrix) - 1
	temp = []
	while count < lenBound:
		temp.append(matrix[row][col])
		count += 1
		if state == 0:
			i = row
			j = col
			while j != 0:
				i += 1
				j -= 1
				temp.append(matrix[i][j])
			result.append(temp)
			temp = []			
			col += 1
			if col == maxCol:
				state = 1
		elif state == 1:
			i = row
			j = col
			while i != maxRow:
				i += 1
				j -= 1
				temp.append(matrix[i][j])
			result.append(temp)
			temp = []
			row += 1
			if row == maxRow:
				state = 2
		else:
			result.append(temp)
	return result
def Solution2(matrix):
	lenBound = len(matrix[0]) + len(matrix) - 1
	i = j = 0
	result = []
	while i < len(matrix):
		temp = []
		k = i
		j = 0
		while k >= 0:
			temp.append(matrix[k][j])
			k -= 1
			j += 1
		result.append(temp)
		i += 1
	j = 1
	while j < len(matrix[0]):
		temp = []
		k = len(matrix) - 1
		a = j
		while  a < len(matrix[0]):
			temp.append(matrix[k][a])
			k -= 1
			a += 1
		result.append(temp)
		j += 1
	return result
def diagonal(a):
	B = [[] for i in range(len(a)*2-1)]
	for i in range(len(a)):
	    for j in range(len(a)):
	        B[i+j].append(a[i][j])
	for i in B:
		i.reverse()
	return B

n = 4
matrix = [[0 for i in range(n)] for j in range(n)]
count = 1
for i in range(n):
	for j in range(n):
		matrix[i][j] = count
		count += 1

for i in range(n):
	temp = []
	for j in range(n):
		temp.append(matrix[i][j])
	print temp
print diagonal(matrix)