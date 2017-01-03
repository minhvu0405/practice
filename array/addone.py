
def plusOne(a):
	carry = 1
	for i in range(len(a)-1,-1,-1):
		m = a[i] + carry
		a[i] = m%10
		carry = m/10
	if carry > 0:
		a = [carry] + a
	return a

a = [9,9,9]
