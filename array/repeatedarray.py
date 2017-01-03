def repeatedNumber(A):
        key = len(A)*[-1]
        value = [0]*len(A)
        for i in range(len(A)):
            n = A[i]
            print n
            key[n-1] = n
            value[n-1] += 1
        dup = miss = -1
        for i in range(len(key)):
            if key[i] == -1:
                miss = i+1
        for i in range(len(value)):
            if value[i] > 1:
                dup = i+1
        result = [dup,miss]
        return result
A = [1,1,3,4] 
print repeatedNumber(A)