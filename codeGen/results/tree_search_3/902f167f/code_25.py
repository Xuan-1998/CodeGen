import math

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        if i == 0:
            dp[i][0] = 0
        else:
            for j in range(m + 1):
                if j == 0 or i == 0:
                    dp[i][j] = 0
                else:
                    for k in range(i):
                        for square_side in range(1, int(math.sqrt((i-k) * (j-k))) + 1):
                            if (i-k) * (j-k) == square_side ** 2:
                                dp[i][j] = min(dp[i][j], dp[k][j-square_side] + 1)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
