import sys
from functools import lru_cache

def read_input():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = [list(map(int, input().split())) for _ in range(n-1)]
        m = int(input())
        prime_factors = list(map(int, input().split()))
        yield n, edges, m, prime_factors

@lru_cache(None)
def prime_factorize(x):
    factors = set()
    i = 2
    while x > 1:
        if x % i:
            i += 1
        else:
            x //= i
            factors.add(i)
    return list(factors)

@lru_cache(None)
def max_distribution_index(n, edges, prime_factors):
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if [i, j] in edges:
                continue
            dp[i][j] = 1 + max(dp[k][i] for k in range(i) if [k, i] in edges)
    return sum(sum(dp[i][j] for j in range(i+1, n+1)) for i in range(1, n))

for T in read_input():
    n, edges, m, prime_factors = T
    print(max_distribution_index(n, edges, prime_factors) % (10**9 + 7))
