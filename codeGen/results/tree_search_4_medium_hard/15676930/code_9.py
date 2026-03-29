from sys import stdin, stdout

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]
c = [int(x) for x in stdin.readline().split()]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = a[i - 1]
    for j in range(1, min(i, n) + 1):
        if j == 1:
            dp[i][j] = max(a[i - 1], b[i - 2])
        else:
            dp[i][j] = max(dp[i - 1][j - 1], c[i - 2]) + a[i - 1]

stdout.write(str(max([dp[n][i] for i in range(1, n + 1)])) + '\n')
