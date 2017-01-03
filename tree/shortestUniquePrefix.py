# Find shortest unique prefix to represent each word in the list.
#
# Example:
#
# Input: [zebra, dog, duck, dove]
# Output: {z, dog, du, dov}
# where we can see that
# zebra = z
# dog = dog
# duck = du
# dove = dov
# NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
class TrieNode:
	def __init__(self):
		self.count = 0
		self.children = {}
	def insert(self,word,index = 0):
		self.count += 1
		if index < len(word):
			character = word[index]
			if character not in self.children:
				self.children[character] = TrieNode()
			node = self.children[character]
			node.insert(word,index+1)
	def search(self,word,index=0):
		if self.count == 1 and index > 0:
			prefix = word[0:index]
		else:
			character = word[index]
			node = self.children[character]
			prefix = node.search(word,index+1)
		return prefix
def shortestUniquePrefix(inputList):
	if inputList is None:
		return
	root = TrieNode()
	for word in inputList:
		root.insert(word)
	result = []
	for word in inputList:
		prefix = root.search(word)
		result.append(prefix)
	return result
A = ['zebra', 'dog', 'duck', 'dove']
print shortestUniquePrefix(A)