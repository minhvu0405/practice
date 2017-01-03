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
def delete(node,data):
	if node is None:
		return node
	if node.val > data:
		node.left = delete(node.left,data)
	elif node.val < data:
		node.right = delete(node.right,data)
	else:
		if node.left is None and node.right is None:
			return None
		elif node.left is None:
			node = node.right
		elif node.right is None:
			node = node.left
		else:
			temp = find_Min(node.right)
			node.val = temp.val
			node.right = delete(node.right,temp.val)
	return node
def search(node,value):
	if node is None:
		return False
	else:
		if node.val == value:
			return True
		elif node.val > value:
			return search(node.left,value)
		else:
			return search(node.right,value)
def find_Min(node):
	if node is None:
		return -1
	while node.left != None:
		node = node.left
	return node
def find_Min_recursive(node):
	if node is None:
		return -1
	elif node.left is None:
		return node.val
	return find_Min_recursive(node.left)
def find_height(node):
	if node is None:
		return -1
	return max(find_height(node.left),find_height(node.right)) + 1	
def print_in_order(node):
	if node is None:
		return
	print_in_order(node.left)
	print node.val
	print_in_order(node.right)
def print_pre_order(node):
	if node is None:
		return
	print node.val
	print_pre_order(node.left)
	print_pre_order(node.right)
def print_post_order(node):
	if node is None:
		return
	print_post_order(node.left)
	print_post_order(node.right)
	print node.val
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

root = Node(3)
insert(root,7)
insert(root,1)
insert(root,5)
insert(root,9)
# print_in_order(root)
delete(root,3)
print_level_order(root)