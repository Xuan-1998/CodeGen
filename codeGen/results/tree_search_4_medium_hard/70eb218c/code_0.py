import sys
from functools import lru_cache

def solve():
    n, x = map(int, input().split())
    @lru_cache(None)
    def dp(n, k):
        if k == 0:
            return -1
        for i in range(10**k-1, 9, -1):
            y = int(str(i) + str(x))
            if len(str(y)) <= n:
                return min(dp(n, k-1-d) + 1 for d in range(k)) or dp(n-k, 0)
        return -1
    print(dp(n, len(str(x))))

if __name__ == "__main__":
    solve()
