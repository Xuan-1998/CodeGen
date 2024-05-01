from sys import stdin

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i <= j:
                dp[i][j] = min(dp[k][k] + (i - k - 1) * (j - k - 1) for k in range(min(i, j)) + [0])
            else:
                dp[i][j] = dp[j][i]

    return dp[n][m]

n, m = map(int, stdin.readline().split())
print(min_squares(n, m))
