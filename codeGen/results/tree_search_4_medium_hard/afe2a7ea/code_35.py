import sys
from functools import lru_cache

def solve():
    n = int(sys.stdin.readline().strip())
    MOD = 998244353
    
    @lru_cache(None)
    def dp(town, power):
        if town == 0:
            return 1
        if town > n or (town < n and power < town):
            return 0
        return (dp(town-1, power) + dp(town-1, power+1)) % MOD
    
    print(dp(n+1, 1))

if __name__ == "__main__":
    solve()
