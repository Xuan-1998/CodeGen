def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][j] = 0 for all j because an empty rectangle or a rectangle with one side can't be tiled by any squares.
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_squares_required = float('inf')
            
            # Consider placing a square with side length min(i, j) in the top-left corner
            if i <= j:
                min_squares_required = min(min_squares_required, 1 + dp[i - min(i, j)][j - min(i, j)])
            
            # Consider placing a square with side length min(j, i) in the left-top corner
            if j <= i:
                min_squares_required = min(min_squares_required, 1 + dp[i][j - min(j, i)])
            
            # Otherwise, consider not placing any squares and recursively calculating the minimum number of squares required for the sub-rectangle.
            min_squares_required = min(min_squares_required, 1 + dp[max(0, i - 1)][max(0, j - 1)])
            
            dp[i][j] = min_squares_required
    
    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
