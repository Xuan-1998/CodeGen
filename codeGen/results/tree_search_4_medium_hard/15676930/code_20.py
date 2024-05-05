import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = c[i - 1]
    for j in range(1, min(i, n)):
        if i == 2:
            dp[i][j] = max(a[i - 1], a[i - 2] + b[i - 1])
        else:
            dp[i][j] = max(a[i - 1] + (dp[i - 1][0] if j > 0 else 0),
                            b[i - 1] + (dp[i - 1][j - 1] if j > 0 else 0),
                            c[i - 1] + (dp[i - 1][j] if j > 0 else 0))

print(max(dp[n]))
