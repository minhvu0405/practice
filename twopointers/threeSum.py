# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
# Example: 
# given array S = {-1 2 1 -4}, 
# and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
def threeSumClosest(A, B):
        A = sorted(A)
        if len(A) < 3:
            return
        if len(A) == 3:
            return sum(A)
        small = float("inf")
        result = None
        for i in range(len(A)):
            l = i+1
            r = len(A)-1
            while l < r:
                s = A[i] + A[l] + A[r]
                if s == B:
                    return s
                if abs(s - B) < small:
                    small = abs(s-B)
                    result = s
                if s > B:
                    r -= 1
                else:
                    l += 1
        return result 
print threeSumClosest([-1,2,1,-4],1)