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
def seperateEvenOdd(A):
    if A == None or A.next == None:
        return A
    listEven = None
    listOdd = Node(0)
    currOdd = listOdd
    curr = A
    while curr and curr.next:
       temp = curr.next
       currOdd.next = curr
       currOdd = currOdd.next
       curr = temp.next
       temp.next = listEven
       listEven = temp
    if curr:
        currOdd.next = curr
        currOdd = currOdd.next
    currOdd.next = None
    return listEven, listOdd.next

def reverseEven(A):
    if A == None or A.next == None:
        return A
    evenList, oddList = seperateEvenOdd(A)
    currEven = evenList
    currOdd = oddList
    result = Node(0)
    curr = result
    while currEven and currOdd:
        curr.next = currOdd
        currOdd = currOdd.next
        curr = curr.next
        curr.next = currEven
        currEven = currEven.next
        curr = curr.next
    if currOdd:
        curr.next = currOdd
        curr = curr.next
    return result.next
A = LinkedList(Node(8))
# A.add(Node(8))
A.add(Node(7))
A.add(Node(6))
A.add(Node(5))
A.add(Node(4))
A.add(Node(3))
A.add(Node(2))
A.add(Node(1))
display(A.getHead())
result = reverseEven(A.getHead())
display(result)