# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
#  Balanced tree : a height-balanced binary tree is defined as a
#  binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example :
#
#
# Given A : [1, 2, 3]
# A height balanced BST  :
#
#       2
#     /   \
#    1     3
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def print_level_order(node):
	if node is None:
		return
	queue = [node]
	while queue:
		top = queue.pop(0)
		print top.val
		if top.left:
			queue.append(top.left)
		if top.right:
			queue.append(top.right)
		
def toBST(array,left,right):
	if left > right:
		return None
	mid = (left + right)/2
	node = Node(array[mid])
	node.left = toBST(array,left,mid-1)
	node.right = toBST(array,mid+1,right)
	return node
def ArrayToBST(array):
	if len(array) < 1:
		return
	root = toBST(array,0,len(array)-1)
	return root
arr = [1,2,3,4,5,6,7,8,9,10]
root = ArrayToBST(arr)
print_level_order(root)