# Given a binary tree, return the zigzag level order traversal of
# its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).
#
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return
#
# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]
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
def zigzagBST(node):
	result = []
	if node is None:
		return result
	currentLevel = [node]
	nextLevel = []
	leftToRight = False
	while currentLevel:
		temp = []
		while currentLevel:
			top = currentLevel.pop()
			if leftToRight:				
				if top.right:
					nextLevel.append(top.right)
				if top.left:
					nextLevel.append(top.left)
			else:
				if top.left:
					nextLevel.append(top.left)
				if top.right:
					nextLevel.append(top.right)
			temp.append(top.val)
		leftToRight = not leftToRight
		result.append(temp)
		currentLevel,nextLevel = nextLevel,currentLevel
	return result

root = Node(8)
insert(root,3)
insert(root,10)
insert(root,1)
insert(root,6)
insert(root,14)
insert(root,13)
insert(root,4)
insert(root,7)
print_in_order(root)
print zigzagBST(root)