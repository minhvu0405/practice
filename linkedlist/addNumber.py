# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation:  342 + 465 = 807
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
def addTwoNumbers(A, B):
    if A == None:
        return B
    if B == None:
        return A
    currA = A
    currB = B
    dummy = Node(0)
    head = dummy
    carry = 0
    temp = 0
    while currA != None or currB != None or carry != 0:
        if currA == None:
            valA = 0
        else:
            valA = currA.val
        if currB == None:
            valB = 0
        else:
            valB = currB.val
        temp = (valA + valB + carry)%10
        carry = (valA + valB + carry)/10
        node = Node(temp)
        head.next = node
        head = node
        if currA:
            currA = currA.next
        if currB:
            currB = currB.next
    return dummy.next
A = LinkedList(Node(1))
B = LinkedList(Node(9))
B.add(Node(9))
B.add(Node(9))
display(A.getHead())
display(B.getHead())
C = addTwoNumbers(A.getHead(),B.getHead())
display(C)