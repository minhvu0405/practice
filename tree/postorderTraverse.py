#               5
#              / \
#             4   8
#            /   / \
#           11  13  9
#          /  \    / \
#         7    2  6   1
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def postorderTraverse(node):
	if node is None:
		return []
	stack = [node]
	result = []
	while stack:
		top = stack[-1]
		if top.left is None and top.right is None:
			m = stack.pop()
			result.append(m.val)
		else:
			if top.right:
				stack.append(top.right)
				top.right = None
			if top.left:
				stack.append(top.left)
				top.left = None
			
	return result
def postorder(node):
	if node is None:
		return
	stack = [node]
	result = []
	while stack:
		top = stack[-1]
		result.append(top.val)
		stack.pop()
		if top.left:
			stack.append(top.left)
		if top.right:
			stack.append(top.right)
	return result[::-1]
def postorder_v2(node):
	if node is None:
		return
	stack = []
	result = []
	while True:
		while node:
			if node.right:
				stack.append(node.right)
			stack.append(node)
			node = node.left
		node = stack.pop()
		if node.right and stack and stack[-1] == node.right:
			stack.pop()
			stack.append(node)
			node = node.right
		else:
			result.append(node.val)
			node = None
		if len(stack) < 1:
			break
	return result

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(9)
root.right.right.right = Node(1)
root.right.right.left = Node(6)
# print postorder(root)
print postorder_v2(root)
# print postorderTraverse(root)