
# Two elements of a binary search tree (BST) are swapped by mistake.
# Tell us the 2 values swapping which the tree will be restored.
#
#  Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# Example :
#
#
# Input :
#          1
#         / \
#        2   3
#
# Output :
#        [1, 2]
#
# Explanation : Swapping 1 and 2 will change the BST to be
#          2
#         / \
#        1   3
# which is a valid BST
class Node:
	def __init__(self,value):
		self.val = value
		self.left = None
		self.right = None
def insert(node,value):
	if node is None:
		return Node(value)
	if value > node.val:
		node.right = insert(node.right,value)
	else:
		node.left = insert(node.left,value)
	return node
def search(node,value):
	if node is None:
		return
	if value == node.val:
		return node
	if value > node.val:
		return search(node.right,value)
	else:
		return search(node.left,value)
def print_in_order(node):
	if node is None:
		return
	print_in_order(node.left)
	print node.val
	print_in_order(node.right)
def recoverBST(node,pre,first,mid,last):
	if node is None:
		return pre,first,mid,last
	pre,first,mid,last = recoverBST(node.left,pre,first,mid,last)
	if pre and node.val < pre.val:
		if first:
			last = node
		else:
			first = pre
			mid = node
	pre = node
	pre,first,mid,last = recoverBST(node.right,pre,first,mid,last)
	return pre,first,mid,last
def fix(first,mid,last):
	if last:
		temp = first.val
		first.val = last.val
		last.val = temp
	else:
		temp = first.val
		first.val = mid.val
		mid.val = temp
root = Node(10)
insert(root,5)
insert(root,8)
insert(root,2)
insert(root,20)
print "Origin: "
print_in_order(root)
print
print "Swap Orgin: 20 and 8"
m = search(root,8)
m.val = 20
n = search(root,20)
n.val = 8
print_in_order(root)
print
pre,first,mid,last = recoverBST(root,None,None,None,None)
# print first,mid,last
fix(first,mid,last)
print "Fixed: "
print_in_order(root)