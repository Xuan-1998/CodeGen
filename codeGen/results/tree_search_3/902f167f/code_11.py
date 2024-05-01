from functools import lru_cache

@lru_cache(None)
def min_squares(n, m):
    if n == 1:
        return m
    if m == 1:
        return n
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # base case: when the current cell is at the edge
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = max(i - 1, j - 1)
            else:
                # consider all possible ways to place a square at the current position
                min_square = float('inf')
                for k in range(1, min(i, j) + 1):
                    min_square = min(min_square, dp[i - k][j] + dp[i][j - k] + (k ** 2))
                dp[i][j] = min_square
    return dp[n][m]

# receive inputs from stdin and print the answer to stdout
n, m = map(int, input().split())
print(min_squares(n, m))
