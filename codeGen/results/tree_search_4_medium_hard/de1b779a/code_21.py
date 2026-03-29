from sys import stdin

def solve():
    n, m, c0, d0 = map(int, stdin.readline().split())
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            ai, bi, ci, di = map(int, stdin.readline().split())
            if i >= c0 and j >= 1:
                dp[i][j] = max(dp[i-1][j], dp[i][ci-1][j-1] + (di-cj) * pj)
            else:
                dp[i][j] = dp[i-1][j]
    return max(dp[n])

print(solve())
