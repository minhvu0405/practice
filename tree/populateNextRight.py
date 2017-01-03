# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#  Note:
# You may only use constant extra space.
# Example :
#
# Given the following binary tree,
#
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
#  Note 1: that using recursion has memory overhead and does not qualify for constant space.
# Note 2: The tree need not be a perfect binary tree.

class Node:
	def __init__(self,data):
		self.val = data
		self.left = None
		self.right = None
		self.next = None
def populateNextRight(node):
	if node is None:
		return
	currentLevel = [node]
	nextLevel = []
	while currentLevel:
		while currentLevel:
			top = currentLevel.pop(0)
			if top.left:
				nextLevel.append(top.left)
			if top.right:
				nextLevel.append(top.right)
			if len(currentLevel) == 0:
				top.next = None
			else:
				top.next = currentLevel[0]
		currentLevel,nextLevel = nextLevel, currentLevel
root = Node(1)
root.left = Node(2)
root.right = Node(3)
l = root.left
r = root.right
l.left = Node(4)
l.right = Node(5)
r.left = Node(6)
r.right = Node(7)
populateNextRight(root)
