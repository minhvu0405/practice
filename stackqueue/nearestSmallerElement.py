def findNearestSmallerElement_BF(A):
	if len(A) < 1:
		return A
	if len(A) == 1:
		return [-1]
	result = [-1]
	for i in range(1,len(A)):
		flag = False
		for j in range(i,-1,-1):
			if A[i] > A[j]:
				result.append(A[j])
				flag = True
				break
		if not flag:
			result.append(-1)
	return result
def findNearestSmallerElement(A):
	if len(A) < 1:
		return A
	if len(A) == 1:
		return [-1]
	result = []
	stack = []
	for i in range(len(A)):
		while stack and stack[-1] >= A[i]:
			stack.pop()
		if not stack:
			result.append(-1)
			stack.append(A[i])
		else:
			result.append(stack[-1])
			stack.append(A[i])
	return result
l1 = [4, 5, 2, 10]
l2 = [3, 2, 1]
print findNearestSmallerElement(l1)
print findNearestSmallerElement(l2)
