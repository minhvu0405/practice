# Write a function that takes an unsigned integer and returns the number of 1 bits it has.
def Solution(A):
	count = 0
	while A > 0:
		count += A & 1
		A >>= 1
	return count
print Solution(11)