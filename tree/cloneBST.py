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
def print_in_order(node):
	if node is None:
		return
	print_in_order(node.left)
	print node.val
	print_in_order(node.right)
def cloneTree(node):
	if node is None:
		return node
	temp = Node(node.val)
	temp.left = cloneTree(node.left)
	temp.right = cloneTree(node.right)
	return temp
root = Node(3)
insert(root,7)
insert(root,1)
insert(root,5)
insert(root,9)
print_in_order(root)
temp = cloneTree(root)
print
print_in_order(temp)