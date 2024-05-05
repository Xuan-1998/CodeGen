# Read input
n, m, c0, d0 = map(int, input().split())
dps = [[0] * (m + 1) for _ in range(n + 1)]

for j in range(m + 1):
    a, b, c, d = map(int, input().split())
    if j > 0:
        dps[0][j] = max(dps[0][j-1], d*(b-a))
    for i in range(1, n+1):
        if j > 0 and i >= c:
            dp[i][j] = max(dp[i-1][j], dp[i-c][j-1] + d*j - c)
        elif j == 0:
            dp[i][j] = 0
print(max(dps[-1]))
