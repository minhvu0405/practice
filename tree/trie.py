class Node:
	def __init__(self):
		self.count = 0
		self.children = {}
	def getCount(self):
		return self.count
	def insert(self,word,index = 0):
		self.count += 1
		if index < len(word):
			character = word[index]
			if character not in self.children:
				self.children[character] = Node()
			node = self.children[character]
			node.insert(word,index+1)
	def search(self,word,index = 0):
		if self.count == 1 and index > 0:
			prefix = word[0:index]
		else: 
			character = word[index]
			node = self.children[character]
			prefix = node.search(word,index+1)
		return prefix
root = Node()
root.insert('minh')
root.insert('dude')
print root.search('duck')
print root.getCount()