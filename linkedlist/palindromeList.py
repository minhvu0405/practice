# Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
class ListNode:
    def __init__(self,x):
        self.head = x
    def add(self,x):
        temp = self.head
        x.next = temp
        self.head = x
    def getHead(self):
        return self.head
def display(head):
    if head == None:
        print "None"
    elif head.next == None:
        print str(head.val)
    else:
        string = ""
        temp = head
        while temp != None:
            string += str(temp.val)
            string += " -> "
            temp = temp.next
        string += "End"
        print string
    print ""
def getLength(X):
    if X == None:
        return 0
    if X.next == None:
        return 1
    count = 0
    while X != None:
        count += 1
        X = X.next
    return count
def reverseList(X):
    if X == None:
        return None
    if X.next == None:
        return X
    head = X
    curr = head.next
    head.next = None
    while curr != None:
        temp = curr.next
        curr.next = head
        head = curr
        curr = temp
    return head
def lPalin(A):
    if A == None or A.next == None:
        return True
    n = getLength(A)
    mid = A
    for i in range(0,n/2):
        mid = mid.next
    reverse = reverseList(mid)
    second = reverse
    first = A
    while first !=  None and second != None:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True

A = ListNode(Node(1))
A.add(Node(8))
A.add(Node(1))
display(A.getHead())
print lPalin(A.getHead())