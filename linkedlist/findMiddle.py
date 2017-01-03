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
def findMiddle(A):
	if A == None or A.next == None:
		return A
	fast = A
	slow = A
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
	return slow
A = LinkedList(Node(6))
A.add(Node(5))
A.add(Node(4))
A.add(Node(3))
A.add(Node(2))
A.add(Node(1))
A.add(Node(0))
display(A.getHead())
mid = findMiddle(A.getHead())
display(mid)