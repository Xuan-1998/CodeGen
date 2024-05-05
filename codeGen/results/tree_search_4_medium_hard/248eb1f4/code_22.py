import sys
from functools import lru_cache

# Pre-compute winners for all possible M values up to a certain limit
M_LIMIT = 1000000
winners = {}
for i in range(1, M_LIMIT + 1):
    winners[(i, 1)] = i % 2

@lru_cache(maxsize=None)
def winner(M, i):
    if i == 1:
        return (M - 1) % 2
    if (M, i) in winners:
        return winners[(M, i)]
    winners[(M, i)] = (winner(M - 1, i - 1) + M) % i
    return winners[(M, i)]

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    print(*[winner(M, x) for x in range(1, X + 1)], sep='\n')
