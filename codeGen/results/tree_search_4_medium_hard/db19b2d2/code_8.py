import sys

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = 1
        for k in range(m):
            if k != h and s[k] >= i-j+1:
                dp[i][j] += dp[i-1][j-1]

p = dp[m][n]
if p > sys.float_info.max:
    print(-1)
else:
    print(p / (2**64))  # Normalize the probability
