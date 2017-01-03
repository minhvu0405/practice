
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers % 1003.
#
# Example :
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def sumRootToLeaf(node,sumTotal):
	if node is None:
		return 0
	sumTotal = sumTotal*10 + node.val
	if node.left is None and node.right is None:
		return sumTotal
	return sumRootToLeaf(node.left,sumTotal) + sumRootToLeaf(node.right,sumTotal)
def findSum(node):
	if node is None:
		return 0
	sumTotal = sumRootToLeaf(node,0)
	return sumTotal
root = Node(6)
root.left = Node(3)
root.left.left = Node(2)
root.left.left.left = Node(6)
root.right = Node(5)
root.right.left = Node(4)


print findSum(root)