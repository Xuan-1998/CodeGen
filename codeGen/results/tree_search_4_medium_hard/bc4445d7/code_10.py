import sys
from functools import lru_cache

@lru_cache(None)
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n + 1) if sieve[p]]

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = []
        for _ in range(n - 1):
            u, v = map(int, input().split())
            edges.append((u, v))
        m = int(input())
        p = list(map(int, input().split()))
        prime_factors = sieve_of_eratosthenes(m)
        k = 1
        for factor in prime_factors:
            k *= factor
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        for u, v in edges:
            for label in range(1, k + 1):
                if (label % p[0]) == 0 and f(u, v, label):
                    dp[u][v][label] = 1
                else:
                    dp[u][v][label] = sum(dp[w][x][k % label] for w, x in edges if w != u and x != v)
        max_index = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                max_index += sum(sum(dp[u][v][k]) for k in range(k + 1))
        print(max_index % (10**9 + 7))

def f(u, v, label):
    if dp[u][v][label]:
        return 1
    for w, x in edges:
        if w != u and x != v:
            if dp[w][x][label]:
                return 1
    return 0

solve()
