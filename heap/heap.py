class Heap:
	def __init__(self):
		self.heapList = [0]
		self.size = 0
	def display(self):
		print self.heapList
	def insert(self,newNode):
		self.heapList.append(newNode)
		self.size = self.size + 1
		self.percUp(self.size)
	
	def percUp(self,i):
		while i/2 > 0:
			if self.heapList[i] < self.heapList[i/2]:
				self.heapList[i/2], self.heapList[i] = self.heapList[i], self.heapList[i/2]
			i = i/2
	def deleteMin(self):
		minimum = self.heapList[1]
		self.heapList[1] = self.heapList.pop()
		self.size -= 1
		self.percDown(1)
		return minimum
	def percDown(self,i):
		tmp = self.heapList[i]
		while i*2 < self.size:
			child = i*2
			if self.heapList[child] > self.heapList[child+1]:
				child += 1
			if tmp > self.heapList[child]:
				self.heapList[i] = self.heapList[child]
			else:
				break
			i = child
		self.heapList[i] = tmp
# myHeap = Heap()
# myHeap.insert(9)
# myHeap.insert(11)
# myHeap.insert(14)
# myHeap.insert(5)
# myHeap.display()
# print myHeap.deleteMin()
# myHeap.display()