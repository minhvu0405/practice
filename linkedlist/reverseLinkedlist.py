# Reverse a linked list. Do it in-place and in one-pass.
def reverseList(A):
    head = A
    if head == None:
        return None
    if head.next == None:
        return head
    temp = head.next
    head.next = None
    while temp != None:
        curr = temp
        temp = temp.next
        curr.next = head
        head = curr
    return head