from functools import lru_cache

@lru_cache(None)
def dfs(seen: set):
    if len(seen) == n:
        return 1.0
    res = 0
    for p, a, b in tickets:
        if {a, b} - seen:
            res += p * (dfs(seen | {a, b})) / (2 ** (n - len(seen)))
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    tickets = [list(map(int, input().split())) for _ in range(n)]
    prob = dfs(set())
    print(f"{prob:.6f}")
