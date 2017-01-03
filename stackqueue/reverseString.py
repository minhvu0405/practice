# Given a string S, reverse the string using stack.
def reverseString(A):
	if len(A) == 0 or len(A) == 1:
		return A
	stack = []
	for i in A:
		stack.append(i)
	s = ""
	for i in range(len(stack)):
		s += str(stack.pop())
	return s
print reverseString("abcdefghi")