# Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def rootToPathSum(node,target):
	result = []
	if node is None:
		return result
	temp = [node.val]
	findAllPathSum(node,target-node.val,result,temp)
	return result
def findAllPathSum(node,target,result,temp):
	if node.left is None and node.right is None and 0 == target:
		result.append(temp[:])
	if node.left:
		temp.append(node.left.val)
		findAllPathSum(node.left,target-node.left.val,result,temp)
		temp.pop()
	if node.right:
		temp.append(node.right.val)
		findAllPathSum(node.right,target-node.right.val,result,temp)
		temp.pop()

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
print rootToPathSum(root,22)