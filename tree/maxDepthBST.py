# Given a binary tree, find its maximum depth.
# The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def maxDepth(node):
	if node is None:
		return 0
	return 1 + max(maxDepth(node.left),maxDepth(node.right))
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
print maxDepth(root)