# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the
# values along the path equals the given sum.
#
# Example :
#
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
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
def pathSum(node,target):
	if node is None:
		return False
	if node.val == target and node.left is None and node.right is None:
		return True
	return pathSum(node.left,target-node.val) or pathSum(node.right,target-node.val)

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)
print_level_order(root)
print pathSum(root,22)