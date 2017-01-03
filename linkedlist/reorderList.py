# Reorder List.
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
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
    pre = A
    while fast and fast.next:
        fast = fast.next.next
        pre = slow
        slow = slow.next
    return pre, slow
def reverseList(A):
    if A == None or A.next == None:
        return A
    curr = None
    head = A
    while head != None:
        temp = head.next
        head.next = curr
        curr = head
        head = temp
    return curr
def reorderList(A):
    if A == None or A.next == None:
        return A
    pre, middle = findMiddle(A)
    pre.next = None
    revList = reverseList(middle)
    list1 = A
    list2 = revList
    dummy = Node(0)
    head = dummy
    i = 1
    while list1 != None and list2 != None:
        if i%2 == 1:
            temp = list1.next
            head.next = list1
            list1.next = None
            list1 = temp
        else:
            temp = list2.next
            head.next = list2
            list2.next = None
            list2 = temp
        head = head.next
        i += 1
    if list2 != None:
        head.next = list2
    return dummy.next
A = LinkedList(Node(7))
A.add(Node(6))
A.add(Node(5))
A.add(Node(4))
A.add(Node(3))
A.add(Node(2))
A.add(Node(1))
# A.add(Node(0))
display(A.getHead())
result = reorderList(A.getHead())
display(result)