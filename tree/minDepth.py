# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
#  NOTE : The path has to end on a leaf node.
# Example :
#
#          1
#         /
#        2
# min depth = 2.
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def minDepth(node):
	if node is None:
		return 0
	if node.left is None and node.right is None:
		return 1
	if node.left is None:
		return 1  + minDepth(node.right)
	if node.right is None:
		return 1 + minDepth(node.left)
	return 1 + min(minDepth(node.left),minDepth(node.right))
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
print minDepth(root)