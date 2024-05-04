import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(10):
        if i == 1:
            dp[i][j] = 1
        else:
            if i >= k and (k-1)*10 + j >= i-1:
                dp[i][j] = (dp[i-1][j//k] * k) % 998244353
            else:
                dp[i][j] = (dp[i-1][j]) % 998244353

print(' '.join(map(str, [sum(row) for row in dp[n]])))
