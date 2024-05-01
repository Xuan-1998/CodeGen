import math

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 0
            else:
                k = math.gcd(i, j)
                for side_length in range(k, 0, -1):
                    if i % side_length == 0 and j % side_length == 0:
                        dp[i][j] = min(dp[i][j], dp[i // side_length][j // side_length] + 1)
    
    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
