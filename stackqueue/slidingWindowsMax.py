# A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. 
# You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position.
# Input: A long array A[], and a window width w
# Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
# Requirement: Find a good optimal way to get B[i]
# Note: if w > length of the array, return 1 element with the max of the array.
def slidingWindowsMax_BF(listInt,size):
	if len(listInt) == 0:
		return listInt
	if size == 0:
		return listInt
	if size > len(listInt):
		return max(listInt)
	result = []
	for i in range(len(listInt)-size+1):
		result.append(max(listInt[i:i+size]))
	return result
def slidingWindowsMax(listInt,size):
	if len(listInt) == 0:
		return listInt
	if size == 0:
		return listInt
	if size > len(listInt):
		return max(listInt)
	deque = []
	result = []
	for i in range(size):
		while deque and listInt[deque[-1]] <= listInt[i]:
			deque.pop()
		deque.append(i)
	result.append(listInt[deque[0]])
	for i in range(size,len(listInt)):
		while deque and deque[0] <= i - size:
			deque.pop(0)
		while deque and listInt[deque[-1]] <= listInt[i]:
			deque.pop()
		deque.append(i)
		result.append(listInt[deque[0]])
	return result
l = [4, 3, 1, 2, 6, 2, 5, 1]
k = 3
print slidingWindowsMax_BF(l,k)
print slidingWindowsMax(l,k)