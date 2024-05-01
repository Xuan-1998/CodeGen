code
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
fixed_path = list(map(int, input().split()))
for u, v in (map(int, input().split()) for _ in range(m)):
    graph[u].append(v)

dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    dp[i][0] = i

for j in range(1, k+1):
    for i in range(j, -1, -1):
        if i == 0:
            dp[i][j] = j
        else:
            dp[i][j] = min(dp[i-1][j-1], 1 + dp[i+1][k])

print(min(max(dp[i][k]) for i in range(1, n+1)), max(min(dp[i][k]) for i in range(1, n+1)))
