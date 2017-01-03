def rotateMatrix(matrix):
	temp = 0
	l = len(matrix)
	for i in range(len(matrix)/2):
		for j in range(i,len(matrix)-i-1):
			temp = matrix[i][j]
			matrix[i][j] = matrix[l-1-j][i]
			matrix[l-1-j][i] = matrix[l-1-i][l-1-j]
			matrix[l-1-i][l-1-j] = matrix[j][l-1-i]
			matrix[j][l-1-i] = temp
m = [[0 for i in range(4)] for j in range(4)]
count = 1
for i in range(len(m)):
	for j in range(len(m)):
		m[i][j] = count
		count += 1
for i in range(len(m)):
	print m[i]
rotateMatrix(m)
print
for i in range(len(m)):
	print m[i]
