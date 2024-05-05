import sys
from functools import lru_cache

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    @lru_cache(None)
    def dfs(i, j):
        if i > j:
            return 1
        res = 0
        for k in range(j+1, min(k+1, n) for k in range(1, j+2)):
            if a[i+k-1] % k == 0:
                res += dfs(i+1, j-k)
        return res

    print(dfs(0, n-1) % (10**9 + 7))

if __name__ == "__main__":
    solve()
