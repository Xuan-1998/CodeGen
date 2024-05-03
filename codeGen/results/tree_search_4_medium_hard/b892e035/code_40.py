from math import prod
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return [p for p, a, b in ticket][j] / sum([p for p, a, b in ticket])
    else:
        p1 = [dp(i - 1, k) * (p if a == k else 0) for k in range(2)]
        return prod(p for p in p1)

T = int(input())
for _ in range(T):
    n = int(input())
    ticket = [list(map(int, input().split())) for _ in range(n)]
    print(sum([dp(i, j) * (p if a == j else 0) for i, (p, a, b) in enumerate(ticket)]) + sum([dp(i, j) * (1 - p) for i, (p, a, b) in enumerate(ticket)]))
