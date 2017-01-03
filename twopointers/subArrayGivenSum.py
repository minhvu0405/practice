import unittest
# Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.
def Solution_BruteForce(A,n):
	if len(A) < 1:
		return -1
	for i in range(len(A)):
		s = A[i]
		if s == n:
			return (i,i)
		for j in range(i+1,len(A)):
			s += A[j]
			if s == n:
				return (i,j)
	return -1
def Solution(A,n):
	if len(A) < 1:
		return -1
	curr = A[0]
	start = 0
	end = 0
	while end < len(A):
		if curr == n and start <= end:
			return (start,end)
		if curr <= n:
			end += 1
			if end < len(A):
				curr += A[end]
		else:
			curr -= A[start]
			start += 1
	return -1
def AnotherSolution(A,n):
	if len(A) < 1:
		return -1
	curr = A[0]
	start = 0
	for i in range(1,len(A)+1):
		while curr > n and start < i - 1:
			curr -= A[start]
			start += 1
		if curr == n:
			return (start,i-1)
		if i < len(A):
			curr += A[i]
	return -1
class myTestCase(unittest.TestCase):
	def testone_BF(self):
		self.assertEqual(Solution_BruteForce([1, 4, 20, 3, 10, 5],33),(2,4))
	def testtwo_BF(self):
		self.assertEqual(Solution_BruteForce([1, 4, 0, 0, 3, 10, 5],7),(1,4))
	def testthree_BF(self):
		self.assertEqual(Solution_BruteForce([1, 4],0),-1)
	def testfour_BF(self):
		self.assertEqual(Solution_BruteForce([1,4,3,5,8,100],100),(5,5))
	def testfive_BF(self):
		self.assertEqual(Solution_BruteForce([1,4,3,5,8,10],31),(0,5))
	def testone(self):
		self.assertEqual(Solution([1, 4, 20, 3, 10, 5],33),(2,4))
	def testtwo(self):
		self.assertEqual(Solution([1, 4, 0, 0, 3, 10, 5],7),(1,4))
	def testthree(self):
		self.assertEqual(Solution([1, 4],0),-1)
	def testfour(self):
		self.assertEqual(Solution([1,4,3,5,8,100],100),(5,5))
	def testfive_BF(self):
		self.assertEqual(Solution([1,4,3,5,8,10],31),(0,5))
	def testone_ano(self):
		self.assertEqual(AnotherSolution([1, 4, 20, 3, 10, 5],33),(2,4))
	def testtwo_ano(self):
		self.assertEqual(AnotherSolution([1, 4, 0, 0, 3, 10, 5],7),(1,4))
	def testthree_ano(self):
		self.assertEqual(AnotherSolution([1, 4],0),-1)
	def testfour_ano(self):
		self.assertEqual(AnotherSolution([1,4,3,5,8,100],100),(5,5))
	def testfive_ano(self):
		self.assertEqual(AnotherSolution([1,4,3,5,8,10],31),(0,5))
# if __name__ == '__main__':
# 	unittest.main()
print mySolution([1, 4],0)