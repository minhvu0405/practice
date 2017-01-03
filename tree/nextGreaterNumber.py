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
def findMin(root):
        if root is None:
            return None
        while root.left:
            root = root.left
        return root
def find(root,data):
    if root is None:
        return None
    if root.val == data:
        return root
    elif root.val < data:
        return find(root.right,data)
    else:
        return find(root.left,data)
def getSuccessor(A, B):
    current = find(A,B)
    if current is None:
        return None
    if current.right:
        return findMin(current.right)
    else:
        successor = None
        ancestor = A
        while ancestor != current:
            if current.val < ancestor.val:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor.val
root = Node(100)
insert(root,98)
insert(root,102)
insert(root,96)
insert(root,99)
insert(root,97)
print getSuccessor(root,97)