import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    dp = [[0.0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1.0

    for i in range(1, m + 1):
        for k in range(min(h - 1, i) + 1):
            if k == 0:
                dp[i][k] = 1.0 - sum(s[:i]) / n
            else:
                dp[i][k] = dp[i-1][k-1] * s[h-1] / (n-k+1)
        for k in range(min(h, i) + 1):
            if k > 0:
                dp[i][k] += dp[i-1][k-1] * s[h-1] / (n-k+1)

    print(max(dp[m]))

solve()
