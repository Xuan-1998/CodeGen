import sys

n, *a = map(int, input().split())
MOD = 10**9 + 7

dp = [[0] * (10**6 + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 10**6 + 1):
        if a[i - 1] % j == 0:
            dp[i][j] = 1
        elif j >= a[i - 1]:
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j // a[i - 1]]) % MOD
        else:
            dp[i][j] = 0

ans = sum(dp[n]) % MOD
print(ans)
