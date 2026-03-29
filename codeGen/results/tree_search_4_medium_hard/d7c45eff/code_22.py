import sys

n, k = map(int, input().split())
s = input()

dp = [[['' for _ in range(k + 1)] for _ in range(n + 1)] for _ in range(2)]

for i in range(n + 1):
    dp[0][i][0] = ''
    if i > 0:
        dp[0][i][0] = dp[0][i - 1][0]

for i in range(1, n + 1):
    for j in range(min(k, n - i) + 1):
        if j <= k - (n - i):
            dp[1][i][j] = dp[0][i - 1][k - j]
        else:
            dp[1][i][j] = dp[0][i][min(j, n - i)]

if k > n:
    print(s * (k // n) + s[:k % n])
else:
    for j in range(min(k, n)):
        if j < min(k, n) and dp[1][n - 1][j] != dp[0][n - 2][min(j, n - 2)]:
            print(dp[1][n - 1][j])
