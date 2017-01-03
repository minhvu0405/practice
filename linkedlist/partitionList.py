# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
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
def partition(A, B):
    if A == None or A.next == None:
        return A
    small = Node(0)
    big = Node(0)
    currSmall = small
    currBig = big
    temp = A
    while temp != None:
        if temp.val >= B:
            currBig.next = temp
            currBig = currBig.next
        else:
            currSmall.next = temp
            currSmall = currSmall.next
        curr = temp
        temp = temp.next
        curr.next = None
    currSmall.next = big.next
    return small.next
A = LinkedList(Node(2))
A.add(Node(5))
A.add(Node(2))
A.add(Node(3))
A.add(Node(4))
A.add(Node(1))
A.add(Node(0))
display(A.getHead())
resullt = partition(A.getHead(),3)
display(resullt)
            