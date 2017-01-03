# Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
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
def rotateRight(A, B):
    if A == None or A.next == None:
        return A
    if B == 0:
        return A
    temp = A
    for i in range(B):
        if temp.next != None:
            temp = temp.next
        else:
            temp = A
    curr = A
    while temp.next != None:
        temp = temp.next
        curr = curr.next
    temp.next = A
    head = curr.next
    curr.next = None
    return head
A = LinkedList(Node(3))
A.add(Node(2))
A.add(Node(1))
display(A.getHead())
res = rotateRight(A.getHead(),7)
display(res)