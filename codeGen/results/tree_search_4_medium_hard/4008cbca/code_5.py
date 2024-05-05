code
def solve():
    n = int(input())
    m = int(input())

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 0 or j == 0:
                dp[i][j] = -1
            else:
                dp[i][j] = min(dp[max(i - 3, 0)][j - 1], dp[i - 1][j] + (i % 4))

    print(dp[n][m])
