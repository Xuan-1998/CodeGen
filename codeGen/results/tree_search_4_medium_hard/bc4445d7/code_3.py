import heapq
from collections import defaultdict

def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    primes = list(map(int, input().split()))

    memo = defaultdict(lambda: float('inf'))

    def dfs(i, j):
        if i > j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        res = float('inf')
        for u, v in edges:
            if u == i and v == j or u == j and v == i:
                continue
            if u < i and v > j:
                res = min(res, dfs(u, i) + dfs(i, j) + dfs(j, v))
        memo[(i, j)] = res
        return res

    res = 0
    for i in range(1, n):
        for j in range(i+1, n):
            res += dfs(i, j)
    print(res % (10**9 + 7))

if __name__ == "__main__":
    solve()
