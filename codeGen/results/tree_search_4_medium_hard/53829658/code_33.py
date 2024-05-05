n = int(input())
roads = []
parent = [i for _ in range(n)]
for _ in range(n - 1):
    si, ti = map(int, input().split())
    roads.append((si, ti))
    parent[si] = ti

dp = [-1] * (n + 1)
for i in range(1, n):
    p = parent[i]
    dp[i] = min(dp[p], 1) if p != -1 else 0

min_inv = float('inf')
capital_cities = []
for i in range(1, n):
    if dp[i] < min_inv:
        min_inv = dp[i]
        capital_cities = [i]

print(min_inv, *capital_cities)
