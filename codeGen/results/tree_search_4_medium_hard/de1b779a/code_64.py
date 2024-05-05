from functools import lru_cache

n, m, c0, d0 = map(int, input().split())
dp = {(0, 0): 0}

@lru_cache(None)
def dp_state(i, j):
    if j == 0:
        return max(dp.get((i-1, 0), 0) or 0, dp.get((c0, 0), 0) or 0)
    else:
        return max(dp.get((i-1, 0), 0) or 0, dp.get((i-ci[j], j-1), 0) or 0) + d[j]

for i in range(1, n+1):
    for j in range(min(j+1, m), -1, -1):
        dp[(i, j)] = dp_state(i, j)

print(max(dp.values()))
