import sys

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(1, n):
    dp[i][i-1] = costs[i-1]

for length in range(2, n):
    for i in range(n-length):
        j = i + length - 1
        min_cost = sys.maxsize
        for k in range(i, j+1):
            cost = costs[k] if (dp[k][k-1] if k > i else 0) + dp[i][k-1] + dp[k+1][j]
            min_cost = min(min_cost, cost)
        dp[i][j] = min_cost

print(dp[0][n-1])
