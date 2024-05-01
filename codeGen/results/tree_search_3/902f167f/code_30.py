import math

def min_squares(n, m):
    dp = [[math.inf] * (m+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                for k in range(i):
                    for square_size in range(1, int(math.sqrt((i-k) * (j-(m-1))))) + 1:
                        if (i-k) * square_size == int(sqrt((i-k) * square_size)):
                            dp[i][j] = min(dp[i][j], dp[k][j-square_size] + 1)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
