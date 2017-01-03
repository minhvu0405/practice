mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
      [1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
      [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
      [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
      [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
      [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
      [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
class Node:
	def __init__(self,v,d):
		self.v = v
		self.d = d
def display():
	for i in mat:
		print i
def isValid(row,col):
	return row >= 0 and col >= 0 and row < len(mat) and col < len(mat[0])
def backtrace(parent,start,end):
	path = [end]
	while path[-1] != start:
		path.append(parent[path[-1]])
	return path[::-1]
def findShortestPath(mat,start,end):
	marked = [[False for i in range(len(mat[0]))] for j in range(len(mat))]
	queue = [Node(start,0)]
	rowNum = [-1,0,0,1]
	colNum = [0,-1,1,0]
	parent = {}
	while queue:
		s = queue.pop(0)
		pos = s.v
		dist = s.d
		marked[pos[0]][pos[1]] = True
		if pos == end:
			return backtrace(parent,start,end)
		for i in range(4):
			row = pos[0] + rowNum[i]
			col = pos[1] + colNum[i]
			if isValid(row,col) and marked[row][col] == False and mat[row][col]:
				cur_node = (row,col)
				parent[cur_node] = s.v
				queue.append(Node(cur_node,dist+1))
	return None
print findShortestPath(mat,(0,0),(3,4))
