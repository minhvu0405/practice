class Node:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.next = None
		self.pre = None
class LRU:
	def __init__(self,capacity):
		self.capacity = capacity
		self.head = None
		self.end = None
		self.map = {}
	def get(self,key):
		if key in self.map:
			node = self.map[key]
			self.remove(node)
			self.setHead(node)
			return node.value
		return -1
	def set(self,key,value):
		if key in self.map:
			node = self.map[key]
			node.value = value
			self.remove(node)
			self.setHead(node)
		else:
			node = Node(key,value)
			if len(self.map) < self.capacity:
				self.setHead(node)
			else:
				self.map.pop(self.end.key)
				self.remove(self.end)
				self.setHead(node)
			self.map[key] = node
	def setHead(self,node):
		if self.head is None:
			self.head = node
			self.end = node
		else:
			node.next = self.head
			self.head.pre = node
			node.next = self.head
			self.head = node
	def remove(self,node):
		if node.pre:
			node.pre.next = node.next
		else:
			self.head = node.next
		if node.next:
			node.next.pre = node.pre
		else:
			self.end = node.pre
	def display(self):
		current = self.head
		s = ""
		while current.next:
			s += str(current.value) + " -> "
			current = current.next
		s += str(current.value)
		print s 
mylru = LRU(3)
mylru.set(3,10)
mylru.set(2,45)
mylru.set(6,100)
mylru.display()
print mylru.get(3)
mylru.display()
mylru.set(8,240)
mylru.display()