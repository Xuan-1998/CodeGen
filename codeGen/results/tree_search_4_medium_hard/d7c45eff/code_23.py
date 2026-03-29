from sys import stdin, maxline
maxline = 5*10**6+1

n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()

dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if i >= n and j >= k:
            dp[i][j] = s[:n]
        elif j < n - i:
            opt1 = (s[:i] + s[-1])[:k]
            opt2 = dp[i-1][j] if i > 0 else ''
            dp[i][j] = min(opt1, opt2)
        else:
            opt2 = dp[i-1][n-i] if i > 0 and j >= n - i else ''
            dp[i][j] = opt2

print(dp[n-1][k])
