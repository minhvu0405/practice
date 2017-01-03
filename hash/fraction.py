# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
def Solve(A,B):
	if B == 0:
		return
	s = ""
	isNegative = False
	if A*B < 0:
		isNegative = True
	A = abs(A)
	B = abs(B)
	m = A/B
	s += str(m)
	remainer = 0
	remainer = A%B
	if remainer != 0:
		s += "."
	else:
		return s
	Dict = {}
	i = len(s)
	while remainer:
		digit = remainer*10/B
		if remainer in Dict:
			s = s[:Dict[remainer]] + "(" + s[Dict[remainer]:] + ")"
			break
		else:
			s += str(digit)
			Dict[remainer] = i
		remainer = (remainer*10)%B
		i += 1
 	if isNegative:
		return "-"+s
	return s
print Solve(1,7)
