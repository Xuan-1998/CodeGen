import sys
from functools import lru_cache

T = int(input())  # Number of test cases

@lru_cache(None)
def dp(i, j):
    if i == 0:  # Base case: no tickets left
        return 1.0
    p1, _, p2 = map(float, input().split())
    if j == 0:
        return max(p1, p2)  # Last ticket, only one number to choose

    seen = set()
    prob = 0.0
    for k in range(2):
        if k not in seen:
            seen.add(k)
            prob += dp(i - 1, j - 1)[k]
    return prob

for _ in range(T):
    n = int(input())
    print(sum([dp(n, i) for i in range(2)]))
