from math import sqrt, ceil

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i * j == 1:
                dp[i][j] = 1
            else:
                for k in range(ceil(sqrt(i)), 0, -1):
                    for m_ in range(ceil(sqrt(j)), 0, -1):
                        if (i - k) * (j - m_) > 0 and dp[k][m_] + 1 < dp[i][j]:
                            dp[i][j] = dp[k][m_] + 1

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
