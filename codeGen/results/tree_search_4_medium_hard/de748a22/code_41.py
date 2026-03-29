import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())
    dp = [[[0, 0] for _ in range(2)] for _ in range(n+1) for _ in range(q+1)]

    for i in range(1, n+1):
        if signs[i-1] == '+':
            dp[i][0][0] += 1
            dp[i-1][0][1] -= 1
        else:
            dp[i][0][0] -= 1
            dp[i-1][0][1] += 1

    for i in range(1, n+1):
        for j in range(1, q+1):
            if signs[i-1] == '+':
                dp[i][j][0] = min(dp[i-1][j][0], dp[i][j-1][1])
                dp[i][j][1] = max(dp[i-1][j][1], 0)
            else:
                dp[i][j][0] = max(dp[i-1][j][0], 0)
                dp[i][j][1] = min(dp[i][j-1][1], dp[i-1][j][0])

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(r, n) - max(l-1, 0))

solve()
