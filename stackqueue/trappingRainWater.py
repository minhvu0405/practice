def Solve_BF(A):
	s = 0
	for i in range(1,len(A)):
		maxLeftBar = 0
		j = i - 1
		while j >= 0:
			maxLeftBar = max(A[j],maxLeftBar)
			j -= 1
		maxRightBar = 0
		k = i + 1
		while k < len(A):
			maxRightBar = max(A[k],maxRightBar)
			k += 1
		maxi = (min(maxLeftBar,maxRightBar) - A[i])
		if maxi < 0:
			maxi = 0
		s += maxi
	return s
def Solve_DP(A):
	right = []
	maxRight = 0
	for i in range(len(A)-1,-1,-1):
		maxRight = max(A[i],maxRight)
		right.append(maxRight)
	right = right[::-1]
	maxi = 0
	s = 0
	maxLeft = 0
	for i in range(0,len(A)):
		maxLeft = max(maxLeft,A[i])
		maxi = min(maxLeft,right[i]) - A[i]
		s += maxi
	return s
def Solve_2P(A):
	left = 0
	right = len(A) - 1
	s = 0
	h = 0
	while left < right:
		if A[left] < A[right]:
			h = max(h,A[left])
			s += h - A[left]
			left += 1
		else:
			h = max(h,A[right])
			s += h - A[right]
			right -= 1
		print s
	return s
def Solve_Stack(A):
	stack = []
	s = 0
	i = 0
	if len(A) == 0:
		return 0
	while i < len(A):
		while stack and A[i] >= A[stack[-1]]:
			p = stack.pop()
			if not stack:
				break
			s += (i - stack[-1] - 1)*(min(A[i],A[stack[-1]]) - A[p])
		stack.append(i)
		i += 1
	return s

t = [2, 0, 2]								# 2
t1 = [3, 0, 0, 2, 0, 4]						# 10
t2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]	# 6
print Solve_Stack(t2)