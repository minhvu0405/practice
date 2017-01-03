# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
def Solution(A):
    if A == None or A.next == None:
        return A
    temp = A
    while temp != None:
        if temp.next and temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return A