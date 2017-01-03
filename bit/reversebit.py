#Reverse bits of an 32 bit unsigned integer
def Solution(A):
	mark = 0
	for i in range(32):
		mark <<= 1
		mark |= (A & 1)
		A >>= 1
	return mark

print Solution(5)
