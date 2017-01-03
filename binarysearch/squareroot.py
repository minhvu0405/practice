# Implement int sqrt(int x).
# Compute and return the square root of x.
# If x is not a perfect square, return floor(sqrt(x))
# Example :
# Input : 11
# Output : 3
import math
def Solution(x):  # Newton's method
	if x < 2:
		return x
	guess = x
	while guess*guess > x:
		guess = (x/guess + guess)/2
	return guess
def Solution2(x):
	if x < 2:
		return x
	start = 0
	end = x
	while start <= end:
		mid = (start+end)/2
		if mid <= x/mid:
			start = mid + 1
			ans = mid
		else:
			end = mid - 1
	return ans
print Solution2(9000000000)
