# Given a binary tree in which each node element contains a number. 
# Find the maximum possible sum from one leaf node to another.
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def maximumPathSumTwoLeaves(node):
	if node is None:
		return 
	maxValue = [-float('inf')]
	findMax(node,maxValue)
	return maxValue[0]
def findMax(node,maxValue):
	if node is None:
		return 0
	if node.left is None and node.right is None:
		return node.val
	left = findMax(node.left,maxValue)
	right = findMax(node.right,maxValue)
	if node.left is not None and node.right is not None:
		maxValue[0] = max(maxValue[0],left+right+node.val)
		return max(findMax(node.left,maxValue),findMax(node.right,maxValue)) + node.val
	if node.left is None:
		return node.val + findMax(node.right,maxValue)
	if node.right is None:
		return node.val + findMax(node.left,maxValue)
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
print maximumPathSumTwoLeaves(root)