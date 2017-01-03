# Given an array of integers, every element appears twice except for one. Find that single one.
def useDictionary(A):
	if len(A) < 1:
		return None
	dic = dict()
	for i in range(len(A)):
		if A[i] not in dic:
			dic[A[i]] = 1
		else:
			dic[A[i]] += 1
	for i in dic:
		if dic[i] == 1:
			return i
	return None
def useBitwise(A):
	if len(A) < 1:
		return None
	result = A[0]
	for i in range(1,len(A)):
		result ^= A[i]
	return result
test = [1,2,3,1,2]
print useDictionary(test)
print useBitwise(test)