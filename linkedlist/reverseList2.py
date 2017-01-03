# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.
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
def reverseList(head):
        if head == None or head.next == None:
            return head
        curr = None
        rest = head
        while rest != None:
            temp = rest
            rest = rest.next
            temp.next = curr
            curr = temp
        return curr
def reverseBetween_sol1(A, m, n):
    if A == None or A.next == None:
        return A
    countm = 1
    countn = 1
    headm = A
    headn = A
    prem = A
    while countn < n:
        if countm < m:
            countm += 1
            prem = headm
            headm = headm.next
        headn = headn.next
        countn += 1
    if m > 1:           # prem and headm are different
        prem.next = None
    last = None
    if headn:
        last = headn.next
        headn.next = None
    reverse = reverseList(headm)
    run = reverse
    while run.next != None:
        run = run.next
    run.next = last
    if m > 1:
        prem.next = reverse
        head = A
    else:               # m = 1 -> prem and headm are the same  
        head = reverse
    return head
def reverseBetween_sol2(A, m, n):
    if A == None or A.next == None:
        return A
    dummy = Node("dump")
    run = dummy
    run.next = A
    for i in range(0,m-1):
        run = run.next
    p = run.next
    curr = None
    for i in range(m,n+1):
        temp = p.next
        p.next = curr
        if i == m:
            tail = p
        curr = p
        p = temp 
    run.next = curr
    tail.next = p
    return dummy.next
A = LinkedList(Node(6))
A.add(Node(5))
A.add(Node(4))
A.add(Node(3))
A.add(Node(2))
A.add(Node(1))
A.add(Node(0))
display(A.getHead())
rev = reverseBetween_sol2(A.getHead(),2,4)
display(rev)
            