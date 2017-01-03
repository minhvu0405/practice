
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example :
#
# Input : [1 2]
# Return :  1
def stock(A):
	if len(A) < 1:
		return 0
	minimum = A[0]
	result = 0
	for i in range(1,len(A)):
		result = max(result,A[i]-minimum)
		minimum = min(minimum,A[i])
	return result
A = [1,3,2,1,6]
print stock(A)