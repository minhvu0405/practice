# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Try solving it using constant additional space.
def detectCycle(A):
    if A == None or A.next == None:
        return A
    fast = A
    slow = A
    isCircle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            isCircle = True
            break
    if isCircle == False:
        return None
    fast = A
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return slow