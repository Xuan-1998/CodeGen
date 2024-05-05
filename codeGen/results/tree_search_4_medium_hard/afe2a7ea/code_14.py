import sys

n = int(sys.stdin.readline())

dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(1, n+2):
    dp[0][i] = 1
    dp[i][0] = 1

for i in range(1, n+2):
    for j in range(1, min(i+1, n+2)):
        if i > 0:
            for k in range(min((i-1)//2, j)+1):
                dp[i][j] += min((i-1)//2, k)*dp[i-1][min(k, i)]

print(dp[n][n+1]%998244353)
