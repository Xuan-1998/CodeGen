import sys
from functools import lru_cache

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    @lru_cache(None)
    def dp(i, k):
        if i == 0:
            return 1 if k >= n else 0
        elif k < 0:
            return 0
        else:
            p = (s[i-1] / sum(s)) * dp(i-1, k-1) + (1 - s[i-1] / sum(s)) * (1 - dp(i-1, k-1))
            return p
    
    ans = 1 - sum(dp(m, n-i) for i in range(n+1))
    
    if ans < 0 or ans > 1:
        print(-1)
    else:
        print('{:.6f}'.format(ans))

if __name__ == "__main__":
    solve()
