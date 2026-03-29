from functools import lru_cache

def maxOr(s):
    n = len(s)
    @lru_cache(None)
    def dp(i, j):
        if i > j:
            return 0
        or_val = int(s[i:j+1], 2) # Convert binary string to integer and perform bitwise OR
        res = or_val
        for k in range(i-1, -1, -1):
            for l in range(j+1, n):
                res = max(res, dp(k, l-1) | or_val)
        return res

    return dp(0, n-1)

n = int(input())
s = input()
print(maxOr(s))
