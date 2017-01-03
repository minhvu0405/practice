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
	slow = A
	fast = A
	pre = A
	while fast and fast.next:
		fast = fast.next.next
		pre = slow
		slow = slow.next
	return slow, pre
def merge(left,right):
	if left == None:
		return right
	if right == None:
		return left
	currLeft = left
	currRight = right
	dummy = Node(0)
	curr = dummy
	while currLeft != None and currRight != None:
		if currLeft.val <= currRight.val:
			curr.next = currLeft
			currLeft = currLeft.next
		else:
			curr.next = currRight
			currRight = currRight.next
		curr = curr.next
	while currLeft != None:
		curr.next = currLeft
		curr = curr.next
		currLeft = currLeft.next
	while currRight != None:
		curr.next = currRight
		curr = curr.next
		currRight = currRight.next
	return dummy.next
def mergeSort(A):
	if A == None or A.next == None:
		return A
	head = A
	mid, pre = findMiddle(A)
	pre.next = None
	left = mergeSort(head)
	right = mergeSort(mid)
	result = merge(left,right)
	return result
A = LinkedList(Node(1))
A.add(Node(5))
A.add(Node(2))
A.add(Node(8))
A.add(Node(0))
A.add(Node(6))
A.add(Node(1))
A.add(Node(19))
display(A.getHead())
result = mergeSort(A.getHead())
display(result)