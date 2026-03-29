import sys
from functools import lru_cache

def solve():
    n = int(input())
    M = list(map(int, input().split()))
    
    @lru_cache(None)
    def dp(i):
        if i == 0:
            return 1
        
        res = 0
        for j in range(n-1, -1, -1):
            if M[j] < M[i]:
                res += dp(j) * (M[:i].count(M[j]) + 1)
        
        return res % (10**9 + 7)

    print(dp(n-1))

if __name__ == "__main__":
    solve()
