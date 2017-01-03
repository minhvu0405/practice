# Convert a BST to a sorted circular doubly-linked list in-place. 
# Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def insert(node,value):
	if node is None:
		node = Node(value)
	else:
		if node.val > value:
			node.left = insert(node.left,value)
		else:
			node.right = insert(node.right,value)
	return node
def print_level_order(node):
	if node is None:
		return
	queue = []
	queue.append(node)
	while queue:
		current = queue.pop(0)
		print current.val
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)
def convertBSTtoLL(node):
	global pre
	global head
	if node is None:
		return None
	convertBSTtoLL(node.left)
	node.left = pre
	if pre:
		pre.right = node
	else:
		head = node
	nextNode = node.right
	head.left = node
	node.right = head
	pre = node
	convertBSTtoLL(nextNode)
	return
def toLL(node):
	global head
	if node is None:
		return
	convertBSTtoLL(node)
	return head
root = Node(4)
insert(root,5)
insert(root,2)
insert(root,1)
insert(root,3)
# print_level_order(root)
pre = None
head = None
head = toLL(root)
print head.val
print head.right.val
print head.right.right.val
print head.right.right.right.val
print head.right.right.right.right.val
print head.right.right.right.right.right.val
print
print head.val
print head.left.val
print head.left.left.val
print head.left.left.left.val
print head.left.left.left.left.val
print head.left.left.left.left.left.val
