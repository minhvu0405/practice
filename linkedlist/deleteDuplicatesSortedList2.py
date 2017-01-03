# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
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

def deleteDuplicates_Dictionary(A):
    if A == None or A.next == None:
        return A
    myDict = dict()
    temp = A
    while temp != None:
        if temp.val not in myDict:
            myDict[temp.val] = 1
        else:
            myDict[temp.val] += 1
        temp = temp.next
    temp = A
    head = A
    while myDict[head.val] > 1:
        head = head.next
        if head == None or head.next == None:
            return head
    temp = head
    while temp != None:
        if myDict[temp.val] > 1:
            temp = temp.next
            pre.next = temp
        else:
            pre = temp
            temp = temp.next
    return head
def deleteDuplicates(A):
    if A == None or A.next == None:
        return A
    dumpNode = Node('Dummy')
    head = dumpNode
    run = dumpNode
    curr = A
    while curr != None:
        if curr.next and curr.val == curr.next.val:
            duplicate = curr
            while curr and duplicate.val == curr.val:
                curr = curr.next
        else:
            run.next = curr
            run = curr
            curr = curr.next
    run.next = None
    return head.next
A = LinkedList(Node(1))
A.add(Node(1))
A.add(Node(1))
A.add(Node(1))
A.add(Node(0))
display(A.getHead())
head = deleteDuplicates(A.getHead())
display(head)