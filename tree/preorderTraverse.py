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
def print_pre_order(node):
	if node is None:
		return
	print node.val
	print_pre_order(node.left)
	print_pre_order(node.right)
def preorderTraverse(node):
	result = []
	if node is None:
		return result
	stack = [node]
	while stack:
		top = stack[-1]
		m = stack.pop()
		result.append(m.val)
		if top.right:
			stack.append(top.right)
		if top.left:
			stack.append(top.left)
	return result

root = Node(3)
insert(root,7)
insert(root,1)
insert(root,5)
insert(root,9)
print_pre_order(root)
print preorderTraverse(root)