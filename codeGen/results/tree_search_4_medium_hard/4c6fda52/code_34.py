import sys

q = int(sys.stdin.readline().strip())
for _ in range(q):
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i
        for j in range(1, min(i, k) + 1):
            dp[i][j] = min(dp[i-1][0], dp[i-1][j-1]) + (s[i-1] != 'RGB'[i%3])
    print(dp[n][k])
