===BEGIN CODE===
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [[0] * (len(costs) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, len(costs) + 1):
        if strings[i - 1].endswith(strings[j - 1]):
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][k] + costs[j - 1] for k in range(j, 0, -1))

answer = float('inf')
for i in range(len(costs) + 1):
    answer = min(answer, dp[n][i])

print(answer if answer != float('inf') else -1)
