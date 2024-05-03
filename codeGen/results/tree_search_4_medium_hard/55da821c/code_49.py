import heapq

m, n = map(int, input().split())
dp = [[float('inf')] * m for _ in range(n)]
plants_to_replant = []

for i in range(n):
    s, x = map(int, input().split())
    plants_to_replant.append((x, s))

plants_to_replant.sort()

for i, (x, s) in enumerate(plants_to_replant):
    for j in range(m):
        if j + 1 == s:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j] if i > 0 else float('inf'), dp[i-1][s-1] if i > 0 else 0) + (dp[i-1][s-1] if i > 0 and dp[i-1][s-1] == 0 else 1)

print(min(dp[-1]))
