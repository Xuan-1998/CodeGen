import math

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            min_squares_needed = float('inf')
            for side_length in range(1, int(math.sqrt(min(i, j))) + 1):
                if i >= side_length ** 2 and j >= side_length:
                    min_squares_needed = min(min_squares_needed, 1 + dp[i - side_length ** 2][j - side_length])
                else:
                    break
            dp[i][j] = min_squares_needed

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
