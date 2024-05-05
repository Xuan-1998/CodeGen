import math
from functools import lru_cache

@lru_cache(maxsize=None)
def C(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

def dp(h, s, n):
    @lru_cache(maxsize=None)
    def rec(i, state1, state2):
        if i >= n:
            return 0
        res = 0
        for j in range(min(s[i], h-state1), -1, -1):
            res += C(n-i-1, j) / C(n, j) * (1 if j > 0 else 1) * rec(i+1, state1+j, state2)
        return res

    return rec(0, 0, 0)

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

if n > sum(s):
    print(-1)
else:
    ans = dp(h-1, s, n)
    print(ans)
