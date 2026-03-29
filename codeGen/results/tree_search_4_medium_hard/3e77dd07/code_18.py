from functools import lru_cache

def isScrambled(s1, s2):
    return sorted(s1) == sorted(s2)

@lru_cache(None)
def dp(i, j):
    if i == 0 and j == 0:
        return True
    if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
        return dp(i-1, j-1)
    if isScrambled(s1[:i], s2[:j]):
        return True
    return False

s1 = input()
s2 = input()

n = len(s1)

for i in range(n):
    for j in range(n):
        if not dp(i+1, j+1) and (i > 0 or j > 0):
            print("False")
            exit(0)
print("True")
