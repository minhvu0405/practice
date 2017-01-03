# Divide two integers without using multiplication, division and mod operator.
# Return the floor of the result of the division.
def Solution(dividend,divisor):
	if divisor == 0:
		return "Error"
	if dividend == divisor:
		return 1
	if dividend == 0 and divisor != 0:
		return 0
	negative = False
	if dividend > 0 and divisor < 0:
		negative = True
	elif dividend < 0 and divisor > 0:
		negative = True
	dividend = abs(dividend)
	divisor = abs(divisor)
	if dividend < divisor:
		return 0
	count = 1
	while dividend >= divisor:
		divisor <<= 1
		count <<= 1
	result = 0
	while count > 1:
		divisor >>= 1
		count >>= 1
		if dividend >= divisor:
			dividend -= divisor
			result += count
	if negative:
		return -result
	if result > 2147483647:
		return 2147483647
	elif result < -2147483648:
		return -2147483648
	return result