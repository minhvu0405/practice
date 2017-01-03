from collections import defaultdict
class Graph:
	def __init__(self,v):
		self.V = v
		self.graph = defaultdict(list)
	def add(self,v1,v2):
		self.graph[v1].append(v2)
	def BFS(self,start):
		mark = [False]*self.V
		print mark
		queue = [start]
		while queue:
			s = queue.pop(0)
			if mark[s] == False:
				mark[s] = True
			else:
				continue
			print s,
			for i in self.graph[s]:
				if mark[i] == False:
					queue.append(i)
		print
	def DFS(self):
		mark = [False]*self.V
		for i in range(self.V):
			if mark[i] == False:
				self.DFS_Utils(i,mark)
	def DFS_Utils(self,s,mark):
		mark[s] = True
		print s,
		for i in self.graph[s]:
			if mark[i] == False:
				self.DFS_Utils(i,mark)
	def printAllPaths(self,s,d):
		visited = [False]*self.V
		path = []
		self.printPath(s,d,visited,path)
	def printPath(self,s,d,visited,path):
		path.append(s)
		visited[s] = True
		if s == d:
			print path
		else:
			for i in self.graph[s]:
				if visited[i] == False:
					self.printPath(i,d,visited,path)
		path.pop()
		visited[s] = False
g = Graph(4)
g.add(0,1)
g.add(0,2)
g.add(0,3)
g.add(2,0)
g.add(2,1)
g.add(1,3)
# g.BFS(2)
g.DFS()
# g.printAllPaths(2,3)


