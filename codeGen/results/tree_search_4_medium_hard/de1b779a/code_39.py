from collections import namedtuple

DPState = namedtuple('DPState', 'dough_left used')

def solve(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 0
    for j in range(n + 1):
        dp[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            ci, bi, ai, di = [int(x) for x in input().split()]
            if ai > 0 and j >= ci:
                # Make buns with the current stuffing type
                profit_with_stuffing = min(ai, (j - ci) // bi) * di + dp[i-1][j-ci*bi]
                profit_without_stuffing = dp[i][j-ci]
                dp[i][j] = max(profit_with_stuffing, profit_without_stuffing)
            else:
                # Do not use the current stuffing type
                dp[i][j] = dp[i][j-ci]

    return dp[m][n]

m, n = [int(x) for x in input().split()]
print(solve(m, n))
