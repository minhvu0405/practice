def maxSubArray(A):
    subSum = finalSum = A[0]
    for i in range(1,len(A)):
        subSum = max(A[i],subSum + A[i])
        finalSum = max(finalSum,subSum)
    return finalSum
A = [-2,1,-3,4,-1,2,1,-5,4]
print maxSubArray(A)