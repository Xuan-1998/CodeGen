import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n)]

for i in range(1, n):
    for j in range(min(i+1, n)+1):
        if j == 0:
            dp[i][j] = max(dp[i-1][j] + a[i], dp[i-2][j] + b[i-1])
        elif j > i:
            dp[i][j] = c[i]
        else:
            dp[i][j] = max(dp[i-1][j-1] + c[i], dp[i-1][j] + a[i])

print(max(dp[-1]))
