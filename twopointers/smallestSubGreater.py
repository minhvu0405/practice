import unittest
# Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.
def Solution_BruteForce(A,x):
	smallest = float('inf')
	for i in range(len(A)):
		s = A[i]
		count = 1
		if s > x:
			return count
		for j in range(i+1,len(A)):
			s += A[j]
			count += 1
			if s > x:
				if count < smallest:
					smallest = count
	return smallest
class myTestCase(unittest.TestCase):
	def testCaseOne_BF(self):
		self.assertEqual(Solution_BruteForce([1, 4, 45, 6, 0, 19],51),3)
	def testCaseTwo_BF(self):
		self.assertEqual(Solution_BruteForce([1, 10, 5, 2, 7],9),1)
	def testCaseThree_BF(self):
		self.assertEqual(Solution_BruteForce([1, 11, 100, 1, 0, 200, 3, 2, 1, 250],280),4)
	def testCaseFour_BF(self):
		self.assertEqual(Solution_BruteForce([1, 5, 4, 10,102],101),1)
# if __name__ == '__main__':
#     unittest.main()