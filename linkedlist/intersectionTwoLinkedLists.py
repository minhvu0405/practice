# Write a program to find the node at which the intersection of two singly linked lists begins.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def getLength(X):
        head = X
        if head == None:
            return 0
        if head.next == None:
            return 1
        count = 0
        while head != None:
            count += 1
            head = head.next
        return count
def getIntersectionNode(A, B):
    a = A
    b = B
    lenA = getLength(A)
    lenB = getLength(B)
    if lenA > lenB:
        diff = lenA - lenB
        for i in range(0,diff):
            a = a.next
    else:
        diff = lenB - lenA
        for i in range(0,diff):
            b = b.next
    while a != None and b != None:
        if a == b:
            return a
        a = a.next
        b = b.next
    return None