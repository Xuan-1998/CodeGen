import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == n:
        return 1 if len(set(tickets[i][1:])) == n - 1 else 0
    
    p = tickets[i][0] * (1 - sum(dp(k, t) for k in range(i) for t in set(tickets[k][1:]) if j not in set(tickets[k][1:])))
    
    return max(p, 0)

n = int(input())
tickets = [list(map(int, input().split())) for _ in range(n)]

ans = sum(dp(k, t) for k in range(n) for t in set(tickets[k][1:]))
print("{:.6f}".format(ans))
