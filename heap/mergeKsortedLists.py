import heapq
# Merge k sorted linked lists and return it as one sorted list.
# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
# will result in
# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
class Node:
	def __init__(self,value):
		self.val = value
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def getHead(self):
		return self.head
	def insert(self,newNode):
		if self.head is None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode
	def display(self):
		node = self.head
		if node is None:
			return
		s = ""
		while node.next:
			s +=  str(node.val) + " -> "
			node = node.next
		s += str(node.val)
		print s
def mergeKSortedLists(inputList):
	heap = []
	for a in inputList:
		m = a.getHead()
		while m:
			heapq.heappush(heap,(m.val,m))
			m = m.next
  	m = []
	while len(heap) > 0:
		n = heapq.heappop(heap)
		m.append(n)	
	head = m[0][1]
	curr = head
	for node in m[1:]:
		curr.next = node[1]
		curr = curr.next
	curr.next = None
	curr = head
	return head
list1 = LinkedList()
list1.insert(Node(20))
list1.insert(Node(10))
list1.insert(Node(1))
list2 = LinkedList()
list2.insert(Node(13))
list2.insert(Node(11))
list2.insert(Node(4))
list3 = LinkedList()
list3.insert(Node(9))
list3.insert(Node(8))
list3.insert(Node(3))
inputList = [list1,list2,list3]
head = mergeKSortedLists(inputList)
curr = head
while curr:
	print curr.val
	curr = curr.next
