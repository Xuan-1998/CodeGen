import sys
from math import log
from functools import reduce

def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    m = int(input())
    prime_factors = list(map(int, input().split()))

    # Calculate sum of logarithms for each edge
    def log_sum(u, v):
        res = 0
        for i in range(m):
            if u < prime_factors[i] and v > prime_factors[i]:
                res += log(prime_factors[i])
            elif u > prime_factors[i] and v < prime_factors[i]:
                res -= log(prime_factors[i])
        return res

    # Calculate maximum possible distribution index
    dp = [[-1] * n for _ in range(n)]
    for u, v in edges:
        if u != v:
            for i in range(n):
                if i != u and i != v:
                    dp[u][i] = max(dp[u][i], log_sum(u, i) + dp[i][v])

    # Print answer
    res = 0
    for u, v in edges:
        if u != v:
            res += dp[u][v]
    print(res % (10**9 + 7))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
