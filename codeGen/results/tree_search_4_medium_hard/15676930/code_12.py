from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = c[i-1]
    dp[i][1] = b[i-1]

for j in range(2, n+1):
    dp[0][j] = 0

for i in range(1, n+1):
    for j in range(2, n+1):
        if j == 2:
            dp[i][j] = max(dp[i-1][j-1] + c[i-1], dp[i-1][j-1] + b[i-1])
        else:
            dp[i][j] = max(dp[i-1][j-1] + a[i-1], dp[i-1][j-2] + max(dp[i-1][j-1] + c[i-1], dp[i-1][j-2] + b[i-1]))

print(max(dp[n]))
