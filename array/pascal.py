class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return len(self.items) == 0
	def enque(self,n):
		self.items.insert(0,n)
	def deque(self):
		return self.items.pop()
	def display(self):
		print self.items
	def reset(self):
		self.items = []
	def peek(self):
		if len(self.items) != 0:
			return self.items[-1]
		else:
			return 0

def Solution(n):
	result = []
	temp = []
	if n <= 0:
		return result
	else:
		for i in range(n):
			result = []
			for j in range(i+1):
				if j == 0 or i == j:
					result.append(1)
				else:
					result.append(temp[i-1][j-1] + temp[i-1][j])
			temp.append(result)
	return temp
result = Solution(5)
print result