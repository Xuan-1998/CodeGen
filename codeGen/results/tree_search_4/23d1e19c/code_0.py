k = int(input())
path = list(map(int, input().split()))
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * (m + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    dp[i][path[i - 1]] = 1
for i in range(k + 1):
    for j in range(1, m + 1):
        if j <= k:
            dp[i][j] = min(dp[max(i - 1, 0)][min(j, k)], dp[i - 1][k]) + (dp[i][path[i - 1]] != j)
        else:
            dp[i][j] = dp[i - 1][k] + (dp[i][path[i - 1]] != j)

print(min(dp[k]), max(dp[k]))
