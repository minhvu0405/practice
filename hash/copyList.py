# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

# Return a deep copy of the list.
def Solve(A):
    Dict = {}
    curr = head
    while curr:
        Dict[curr] = RandomListNode(curr.label)
        curr = curr.next
    curr = head
    while curr:
        m = Dict[curr]
        if curr.next in Dict:
            m.next = Dict[curr.next]
        else:
            m.next = None
        if curr.random in Dict:
            m.random = Dict[curr.random]
        else:
            m.random = None
        curr = curr.next
    newhead = Dict[head]
    return newhead