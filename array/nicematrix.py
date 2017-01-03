def display(m,x):
	for i in range(x):
		print m[i]
def solution(m,n):
	x = n*2-1
	for i in range(n):
		for j in range(n):
			if i >= j:
				m[i][j] = n - j
			else:
				m[i][j] = n - i
	for i in range(n):
		for j in range(x-1,0,-1):
			m[i][j] = m[i][x-1-j]
	for i in range(x-1,0,-1):
		for j in range(x):
			m[i][j] = m[x-1-i][j]
	return m
def solution2(m,n):
	minCol = 0
	maxCol = len(m[0]) - 1
	minRow = 0
	maxRow = len(m) - 1
	lenMatrix = len(m[0])*len(m)
	print "lenMatrix: ",lenMatrix 
	result = []
	state = 0
	col = row = 0
	count = 0
	while count < lenMatrix:
		m[row][col] = n
		count += 1
		if state == 0:
			col += 1
			if col == maxCol:
				state = 1
		elif state == 1:
			row += 1
			if row == maxRow:
				state = 2
		elif state == 2:
			col -= 1
			if col == minCol:
				state = 3
		else:
			row -= 1
			if row == minRow:
				state = 0
				minRow += 1
				minCol += 1
				maxRow -= 1
				maxCol -= 1
				col += 1
				row += 1
				n -= 1

	print "count: ",count
	return m
n = 3
x = n*2-1
m = [[0 for i in range(x)] for j in range(x)]
a = solution2(m,n)
display(a,x)

