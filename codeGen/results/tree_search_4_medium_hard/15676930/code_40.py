from sys import stdin

n = int(stdin.readline())
a, b, c = map(int, stdin.readline().split()), map(int, stdin.readline().split())

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = 0
    for j in range(1, min(i+1, n)+1):
        if j == 1:
            dp[i][j] = a[i]
        elif j == i:
            dp[i][j] = c[i]
        else:
            dp[i][j] = max(dp[i-1][k-1] + b[i] for k in range(j))

print(dp[n][n])
