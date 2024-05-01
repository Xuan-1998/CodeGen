from sys import stdin

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]

dp = [[0] * 106 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 106):
        if a[i - 1] == j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][a[i - 1] - 1] + 1)

print(max(max(row) for row in dp))
