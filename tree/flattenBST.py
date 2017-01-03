#               5
#              / \
#             4   8
#            /   / \
#           2  	6  	10
#          / \     / \
#         1   3   9   11
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
# Inplace Solution
def sol(root):
    root1 = root
    while root:
        if root.left is None:
            root = root.right
        else:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            tmp.right = root.right
            root.right = root.left
            root.left = None
    return root1
# Stack based Solution
def preorderTraverse(root):
	node = root
	if node is None:
		return
	stack = [node]
	result = []
	while stack:
		top = stack.pop()
		result.append(top)
		if top.right:
			stack.append(top.right) 
		if top.left:
			stack.append(top.left)
	return result
def flatten(listNodes):
	for i in range(len(listNodes)-1):
		curr = listNodes[i]
		curr.left = None
		curr.right = listNodes[i+1]
	last = listNodes[-1]
	last.left = None
	last.right = None
	return listNodes[0]
def display(node):
	while node.right:
		print node.val
		node = node.right
	print node.val	

root = Node(5)
insert(root,4)
insert(root,8)
insert(root,6)
insert(root,10)
insert(root,11)
insert(root,9)
insert(root,2)
insert(root,1)
insert(root,3)
m = sol(root)
result = preorderTraverse(root)
flattenRoot = flatten(result)
display(flattenRoot)
# display(m)
