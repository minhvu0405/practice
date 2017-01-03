# Given preorder and inorder traversal of a tree, construct the binary tree.
#
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input :
#         Preorder : [1, 2, 3]
#         Inorder  : [2, 1, 3]
#
# Return :
#             1
#            / \
#           2   3
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def print_in_order(root):
	if root is None:
		return
	print_in_order(root.left)
	print root.val
	print_in_order(root.right)
def search(array,value,left,right):
	if array is None:
		return
	for i in range(left,right+1):
		if array[i] == value:
			return i
def create(preorder,inorder,left,right):
	if left > right:
		return None
	node = Node(preorder[constructTree.index])
	constructTree.index += 1 
	if left == right:
		return node
	newindex = search(inorder,node.val,left,right)
	node.left = create(preorder,inorder,left,newindex-1)
	node.right = create(preorder,inorder,newindex+1,right)
	return node
def constructTree(preorder,inorder):
	if preorder is None or inorder is None:
		return
	root = create(preorder,inorder,0,len(preorder)-1)
	return root
inorder = ['D', 'B' ,'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
constructTree.index = 0
root = constructTree(preorder,inorder)
print_in_order(root)