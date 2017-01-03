# You are given a string, S, and a list of words, L, that are all of the same length.
# Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
def Solve_hash(S,L):
    hashSum = sum([hash(i) for i in L])
    lenWord = len(L[0])
    result = []
    for i in range(len(S)):
        j = i
        s = 0
        count = 0
        while j < len(S):
            word = S[j:j+lenWord]
            s += hash(word)
            count += 1
            if count == len(L):
                if s == hashSum:
                    result.append(i)
                break
            j += lenWord
    return result
S = "barfoothefoobarman"
# S = "foobar"
L = ["foo", "bar"]
print Solve_hash(S,L)