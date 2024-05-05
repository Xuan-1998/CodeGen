import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = a[i-1]
    dp[i][i] = b[i-1]

for i in range(2, n+1):
    for j in range(1, min(i, n)+1):
        if j == 1:
            dp[i][j] = max(a[i-1], dp[i-1][0])
        else:
            dp[i][j] = max(dp[i-1][min(j-1, i-2)] + a[i-1], 
                            b[i-1] + dp[i-1][max(0, j+1)])

print(max(dp[n]))
