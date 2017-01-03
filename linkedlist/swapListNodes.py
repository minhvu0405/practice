# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
class Node():
    def __init__(self,value):
        self.val = value
        self.next = None
class LinkedList():
    def __init__(self,new):
        self.head = new
    def add(self,x):
        x.next = self.head
        self.head = x
    def getHead(self):
        return self.head
def display(head):
    if head == None:
        print "Empty List"
        return
    if head.next == None:
        print str(head.val) + " -> End"
        print "Done"
        return
    string = ""
    temp = head
    while temp != None:
        string += str(temp.val)
        string += " -> "
        temp = temp.next
    string += "End"
    print string
    print "Done"
def swapNodes(A):
	if A == None or A.next == None:
		return A
	dummy = Node(0)
	dummy.next = A
	curr = dummy
	while curr.next != None and curr.next.next != None:
		curr.next = swap(curr.next,curr.next.next)
		curr = curr.next.next
	return dummy.next
def swap(node1,node2):
	node1.next = node2.next
	node2.next = node1
	return node2
A = LinkedList(Node(1))
A.add(Node(5))
A.add(Node(2))
A.add(Node(8))
A.add(Node(0))
A.add(Node(6))
A.add(Node(1))
A.add(Node(19))
display(A.getHead())
result = swapNodes(A.getHead())
display(result)