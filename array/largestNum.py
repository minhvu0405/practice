def mycmp(a,b):
	if int(a+b) > int(b+a):
		return 1
	elif int(a+b) == int(b+a):
		return 0
	else:
		return -1
def largestNumber(A):
        a = map(str, A)
        a.sort(mycmp, reverse = True)
        return ''.join(a).lstrip('0') or '0'
A = [54,546,548,60]
a = largestNumber(A)
print a

