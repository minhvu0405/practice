
#               5
#              / \
#             9   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  3   1
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def findPath(node,target,path):
	if node is None:
		return False
	path.append(node.val)
	if node.val == target:
		return True
	if findPath(node.left,target,path) or findPath(node.right,target,path):
		return True
	path.pop()
	return False
def findLCA(node,A,B):
	pathA = []
	pathB = []
	if not findPath(node,A,pathA) or not findPath(node,B,pathB):
		return -1
	i = 0
	while i < len(pathA) and i < len(pathB):
		if pathA[i] != pathB[i]:
			break
		i += 1
	return pathA[i-1]
root = Node(5)
root.left = Node(9)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)
root.right.right.left = Node(3)
print findLCA(root,13,40)