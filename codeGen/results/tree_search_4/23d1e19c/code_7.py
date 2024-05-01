n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

dp = [[float('inf')] * (n+1) for _ in range(n+1)]
max_dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i-1] = 0
    max_dp[i][i-1] = 0

dp[k][n] = 0
max_dp[0][n] = 0

answer = float('inf')
for j in range(n, k-1, -1):
    for i in range(j+1):
        dp[j][i] = min(dp[i][j-1], 1 + dp[j+1][k]) if i > j else dp[i][j-1]
        max_dp[j][i] = max(max_dp[i][j-1], 1 + max_dp[j+1][k]) if i > j else max_dp[i][j-1]

answer = min(answer, dp[k][n] - max_dp[0][n])
print(answer)
