import sys

def solve():
    n, q = map(int, sys.stdin.readline().split())
    signs = list(sys.stdin.readline().strip())
    dp = [[0, 0] for _ in range(n+1)]

    for i in range(1, n+1):
        if signs[i-1] == '+':
            dp[i][0] = dp[i-1][0]
            dp[i][1] = min(dp[i-1][1], dp[i-1][0])
        else:
            dp[i][0] = min(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][1]

    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        if sum(signs[l:r+1]) == 0:
            print(min(dp[r][0], dp[r][1]))
        else:
            print(min(dp[max(0, l-1)][1], dp[max(0, l-1)][0]))

solve()
