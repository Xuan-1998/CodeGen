from sys import stdin

n = int(stdin.readline().strip())
p = list(map(int, stdin.readline().strip().split()))

dp = [[False] * (2*n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = p[:i] == []
    if not dp[i][0]:
        dp[i][0] = False

for j in range(2*n + 1):
    dp[0][j] = p[:j] == []

for i in range(1, n + 1):
    for j in range(1, 2*n + 1):
        if p[i-1] < p[j-1]:
            dp[i][j] = dp[i-1][j-1]
        elif p[i-1] > p[j-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = (dp[i-1][j-1] or dp[i-1][j])

print("YES" if dp[n][2*n] else "NO")
