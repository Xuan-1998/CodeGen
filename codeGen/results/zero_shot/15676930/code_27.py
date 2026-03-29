import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (1 << n) for _ in range(n)]

for i in range(1, n):
    dp[i][0] = a[i]
    for j in range(1, 1 << n):
        if ((j >> (i - 1)) & 1) and ((j >> i) & 1):  # both full
            dp[i][j] = max(dp[i-1][j>>1] + c[i], dp[i-1][(j<<1)|1] + b[i])
        elif ((j >> (i - 1)) & 1):  # one full
            dp[i][j] = max(dp[i-1][j>>1] + a[i], dp[i-1][(j<<1)|1] + c[i])
        else:  # both hungry
            dp[i][j] = max(dp[i-1][j|1] + b[i], dp[i-1][j] + a[i])

print(max(dp[-1]))
