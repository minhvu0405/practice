# Given a linked list, remove the nth node from the end of list and return its head.

# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
def Solution(A,B):
	temp = A
	count = 0
	while count < B:
	    count += 1
	    temp = temp.next
	    if temp == None:
	        head = A
	        head = head.next
	        return head
	curr = A
	while temp != None:
	    temp = temp.next
	    pre = curr
	    curr = curr.next
	pre.next = curr.next
	return A