import sys
from functools import lru_cache

def solve(n, k):
    @lru_cache(None)
    def dp(i, j):
        if i < 0:
            return 1
        x = 1 << k - 1
        res = 0
        while x <= i:
            if (x & j) >= j and ((x ^ j) >= j):
                res += dp(x - 1, j)
            x <<= 1
        return res

    ans = 0
    for j in range(2**k):
        ans += dp(n - 1, j)
    return ans % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
