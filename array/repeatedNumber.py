# You're given a read only array of integers.
# Find out if any integer occurs more than n/3 times in array in linear time and constant additional space.
# If so, return the integer. If not, return - 1
# If there are multiple solutions, return any one.
def Solution(arr):
	num1 = 0
	num2 = 0
	counter1 = 0
	counter2 = 0
	for i in arr:
		if num1 == i:
			counter1 += 1
		elif num2 == i:
			counter2 += 1
		elif counter1 == 0:
			counter1 = 1
			num1 = i
		elif counter2 == 0:
			counter2 = 1
			num2 = i
		else:
			counter1 -= 1
			counter2 -= 1
	counter1 = 0
	counter2 = 0
	for i in arr:
		if i == num1:
			counter1 += 1
		elif i == num2:
			counter2 += 1
	if counter1 > len(arr)/3: 
		return num1
	if counter2 > len(arr)/3:
		return num2
	return -1
arr = [1,2,3,1,1]
print Solution(arr)