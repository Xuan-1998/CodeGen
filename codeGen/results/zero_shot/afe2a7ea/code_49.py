import sys
from functools import lru_cache

def solve(n):
    MOD = 998244353
    @lru_cache(None)
    def count_ways(k):
        if k < 0:
            return 1
        if k > n or k == 0:
            return 0
        res = 0
        for i in range(k+1):
            res += count_ways(i) * (k - i) % MOD
        return res

    ways = count_ways(n)
    return ways

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(solve(n))
