#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def inorder(node):		# modify the tree
	if node is None:
		return
	stack = [node]
	result = []
	while stack:
		top = stack[-1]
		if top.left:
			stack.append(top.left)
			top.left = None
		else:
			m = stack.pop()
			result.append(m.val)
			if m.right:
				stack.append(m.right)
	return result
def inorderTraverse(node):
	if node is None:
		return
	stack = []
	result = []
	current = node
	while len(stack) != 0 or current is not None:
		if current is not None:
			stack.append(current)
			current = current.left
		else:
			current = stack.pop()
			result.append(current.val)
			current = current.right
	return result
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)
root.right.right.left = Node(5)
print inorderTraverse(root)