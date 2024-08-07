from sys import stdin

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]
c = [int(x) for x in stdin.readline().split()]

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][0], c[i-1])
    if i > 1:
        dp[i][0] = min(max(c[i-1], dp[i-2][0]), a[i-1])
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], b[i-j])

print(dp[n][n])
