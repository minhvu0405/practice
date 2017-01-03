# Given a binary search tree T, where each node contains a positive integer,
# and an integer K, you have to find whether or not there exist two different
# nodes A and B such that A.value + B.value = K.
#
# Return 1 to denote that two such nodes exist. Return 0, otherwise.
#
# Notes
# - Your solution should run in linear time and not take memory more than O(height of T).
# - Assume all values in BST are distinct.
#
# Example :
#
# Input 1:
#
# T :       10
#          / \
#         9   20
#
# K = 19
#
# Return: 1
#
# Input 2:
#
# T:        10
#          / \
#         9   20
#
# K = 40
#
# Return: 0
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
def createStack(node):
	small = node
	big = node
	stackSmall = []
	stackBig = []
	while small:
		stackSmall.append(small)
		small = small.left
	while big:
		stackBig.append(big)
		big = big.right
	return stackSmall,stackBig
def getNext(stack):
	node = stack.pop()
	successor = node.val
	if node.right:
		node = node.right
		while node:
			stack.append(node)
			node = node.left
	return successor
def getPrevious(stack):
	node = stack.pop()
	predecessor = node.val
	if node.left:
		node = node.left
		while node:
			stack.append(node)
			node = node.right
	return predecessor
def find2sum(node,target):
	if node is None:
		return 0
	stackSmall,stackBig = createStack(node)
	a = getNext(stackSmall)
	b = getPrevious(stackBig)
	while a < b:
		if a + b == target:
			return 1
		elif a + b > target:
			b = getPrevious(stackBig)
		else:
			a = getNext(stackSmall)
	return 0
root = Node(7)
insert(root,10)
insert(root,9)
insert(root,20)
insert(root,1)
print find2sum(root,19)
