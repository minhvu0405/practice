# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
def mergeTwoLists(A, B):
    if A == None:
        return B
    if B == None:
        return A
    currA = A
    currB = B
    if currA.val < currB.val:
        headFinal = currA
        currA = currA.next
    else:
        headFinal = currB
        currB = currB.next
    currFinal = headFinal
    while currA != None and currB != None:
        if currA.val < currB.val:
            currFinal.next = currA
            currFinal = currFinal.next
            currA = currA.next
        else:
            currFinal.next = currB
            currFinal = currFinal.next
            currB = currB.next
    while currA != None:
        currFinal.next = currA
        currFinal = currFinal.next
        currA = currA.next
    while currB != None:
        currFinal.next = currB
        currFinal = currFinal.next
        currB = currB.next
    return headFinal