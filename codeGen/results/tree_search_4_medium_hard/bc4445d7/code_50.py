from functools import lru_cache
import sys

def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    m = int(input())
    primes = list(map(int, input().split()))
    k = eval('*'.join(map(str, primes)))

    memo = {}
    @lru_cache(None)
    def f(i):
        if i == n:
            return 0
        if (i, ) in memo:
            return memo[(i, )]
        res = 1e9
        for j in range(n - 1):
            if edges[j][0] == i or edges[j][1] == i:
                res = min(res, f(edges[j][0]) + f(edges[j][1]) - (edges[j][0] < i))
        memo[(i, )] = res
        return res

    print((f(1) % (10**9 + 7)))

if __name__ == "__main__":
    solve()
