from sys import stdin

n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()

dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = []

for i in range(1, n+1):
    for j in range(min(i, k), -1, -1):
        if s[i-1] <= min(dp[i-1]):
            dp[i][j] = dp[i-1][j-1] + [s[i-1]]
        else:
            dp[i][j] = dp[i-1][j]

print(''.join(min(dp[n], key=lambda x: (''.join(x), len(x))) [-k:]))
