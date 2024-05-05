import sys

n = int(input())
m = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(i):
        if m[j] < i:
            dp[i][j] += dp[i - 1][max(0, j - (i - m[j]))]
        else:
            dp[i][j] = dp[i - 1][j]

ans = sum(dp[n][k] for k in range(n + 1))
print(ans % (10**9 + 7))
