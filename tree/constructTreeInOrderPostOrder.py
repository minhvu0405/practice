
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input :
#         Inorder : [2, 1, 3]
#         Postorder : [2, 3, 1]
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
def print_pre_order(root):
	if root is None:
		return
	print root.val
	print_pre_order(root.left)
	print_pre_order(root.right)
def search(array,data,left,right):
	for i in range(left,right+1):
		if array[i] == data:
			return i
def createTree(inorder,postorder,left,right):
	if left > right:
		return None
	node = Node(postorder[constructTree.index])
	constructTree.index -= 1
	if left == right:
		return node
	nextNodeIndex = search(inorder,node.val,left,right)
	node.right = createTree(inorder,postorder,nextNodeIndex+1,right)
	node.left = createTree(inorder,postorder,left,nextNodeIndex-1)
	return node	
def constructTree(inorder,postorder):
	if inorder is None or postorder is None:
		return 
	root = createTree(inorder,postorder,0,len(postorder)-1)
	return root
inorder   = [4, 8, 2, 5, 1, 6, 3, 7]
postorder = [8, 4, 5, 2, 6, 7, 3, 1] 
constructTree.index = len(postorder) - 1
root = constructTree(inorder,postorder)
print_pre_order(root)
