import sys

n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][1] = 10 ** i

for i in range(2, n + 1):
    for j in range(i, -1, -1):
        if j == 0:
            break
        dp[i][j] = sum(dp[i-1][k] for k in range(j, min(j+1, n) + 1))
        dp[i][j] %= 998244353

ans = ' '.join(str(count) for count in [dp[n][i] % 998244353 for i in range(1, n + 1)])
print(ans)
