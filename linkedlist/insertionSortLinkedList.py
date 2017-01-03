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
def insertionSort(A):
    if A == None or A.next == None:
        return A
    curr = A
    result = None
    while curr != None:
        temp = curr.next
        result = sortList(curr,result)
        curr = temp
    return result
def sortList(node,result):
    if node == None:
        return
    if result == None:
        node.next = result
        result = node
        return result
    else:
        head = result
        pre = result
        curr = result
        while curr != None:
            if node.val > curr.val:
                pre = curr
                curr = curr.next
            else:
                if pre == curr:        # Add to the beginning of the linked list
                    node.next = curr
                    head = node
                    return head
                else:                  # Add to middle of the linked list
                    pre.next = node
                    node.next = curr
                    return head
        node.next = None               
        pre.next = node                # Add to the end of the linked list
        return head
A = LinkedList(Node(1))
A.add(Node(5))
A.add(Node(2))
A.add(Node(8))
A.add(Node(0))
A.add(Node(6))
A.add(Node(1))
A.add(Node(19))
display(A.getHead())
result = insertionSort(A.getHead())
display(result)