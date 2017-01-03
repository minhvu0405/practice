# You have to paint N boards of length [A0,A1,...,AN-1]. 
# There are K painters available and you are also given how much time a painter takes to paint 1 unit of board. 
# You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.
# Input :
# K : Number of painters
# T : Time taken by painter to paint 1 unit of board
# L : A List which will represent length of each board
# Output:
# return minimum time to paint all boards % 10000003
def Solution(K,T,L):
	small = max(L)
	big = sum(L)
	while small < big:
		mid = (small+big)/2
		n = calculateNeededPainters(mid,L)
		if n <= K:
			big = mid
		else:
			small = mid + 1
	return small*T % 10000003
def calculateNeededPainters(mid,L):
	numPainters = 1
	total = 0
	for i in L:
		total += i
		if total > mid:
			total = i
			numPainters += 1
	return numPainters
A = 3
B = 10
C = [ 640, 435, 647, 352, 8, 90, 960, 329, 859 ]
print Solution(A,B,C)
