
world = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
    	[1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
def isValid(row,col,world):
	return row >= 0 and row < len(world) and col >= 0 and col < len(world[0])
def countIsland_BFS(world):
	rowNum = [-1, -1, -1, 0, 1, 1,  1,  0]
	colNum = [-1,  0,  1, 1, 1, 0, -1, -1]
	marked = [[False for i in range(len(world[0]))] for j in range(len(world))]
	count = 0
	queue = []
	for i in range(len(world)):
		for j in range(len(world[i])):
			if marked[i][j] == False and world[i][j] == 1:
				n = (i,j)
				queue.append(n)
				while queue:
					s = queue.pop(0)
					marked[s[0]][s[1]] = True
					for k in range(8):
						row = s[0] + rowNum[k]
						col = s[1] + colNum[k]
						if isValid(row,col,world) and marked[row][col] == False and world[row][col] == 1:
							m = (row,col)
							queue.append(m)
				count += 1
	return count
def countIsland_DFS(world):
	count = 0
	marked = [[False for i in range(len(world[0]))] for j in range(len(world))]
	for i in range(len(world)):
		for j in range(len(world[i])):
			if marked[i][j] == False and world[i][j] == 1:
				DFS(i,j,marked,world)
				count += 1
	return count
def DFS(row,col,marked,world):
	rowNum = [-1, -1, -1, 0, 1, 1,  1,  0]
	colNum = [-1,  0,  1, 1, 1, 0, -1, -1]
	marked[row][col] = True
	for i in range(8):
		if isValid(row+rowNum[i],col+colNum[i],world) and marked[row+rowNum[i]][col+colNum[i]] == False and world[row+rowNum[i]][col+colNum[i]] == 1:
			DFS(row+rowNum[i],col+colNum[i],marked,world)

def display(matrix):
	for i in range(len(matrix)):
		print matrix[i]
print countIsland_BFS(world)
print countIsland_DFS(world)