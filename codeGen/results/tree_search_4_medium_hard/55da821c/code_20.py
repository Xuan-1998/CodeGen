import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(i - 1, n + 1):
        last_species = dp[i - 1][j - 1][0]
        replant_cost = 1 if abs(s[j] - i) > i - 1 else 0
        not_replant_cost = dp[i - 1][j - 1][1]

        dp[i][j] = min(dp[i - 1][j - 1][1] + replant_cost, not_replant_cost)

print(dp[m][n])
