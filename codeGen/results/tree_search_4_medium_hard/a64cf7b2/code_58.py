import sys

n, m, T = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    dp[u][v] = min(dp.get((u, v), float('inf')), t)

k = 0
route = [1]
i = 1
prev = -1

while i <= n and prev != n:
    max_next = 0
    for j in range(1, n + 1):
        if dp[i][j] > 0 and j not in route:
            max_next = max(max_next, dp[i][j])
    if max_next == 0:
        break
    prev = i
    i += 1
    k += 1
    route.append(i)

print(k)
print(*route[1:])
