from sys import stdin

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]
c = [int(x) for x in stdin.readline().split()]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = max(sum(c[:i]), sum(b[:i]))
    for j in range(1, min(i, n) + 1):
        dp[i][j] = max(dp[i-1][j-1] + c[i-1] if j > 0 else a[i-1], dp[i-1][0] + b[i-1])

print(max(dp[n]))
