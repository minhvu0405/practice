# Write a program to validate if the input string has redundant braces?
# Return 0/1 
#  0 -> NO 1 -> YES 
# Input will be always a valid expression
# and operators allowed are only + , * , - , /
# Example:
# ((a + b)) has redundant braces so answer will be 1
# (a + (a + b)) doesn't have have any redundant braces so answer will be 0
def isRedundant(A):
	if len(A) < 1:
		return A
	stack = []
	for i in range(len(A)):
		if A[i] != ")":
			stack.append(A[i])
		else:
			flag = False
			while stack and stack[-1] != "(":
				if stack[-1] in "+-*/":
					flag = True
				stack.pop()
			if not flag:
				return 1
			if stack:
				stack.pop()
	return 0
s = "(a+b + (c))"
print isRedundant(s)