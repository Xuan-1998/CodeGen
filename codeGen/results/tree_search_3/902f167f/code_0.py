def minSquares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base cases: dp[0][j] and dp[i][0]
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(n + 1):
        dp[i][0] = i
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Minimum number of squares to tile up to (i, j)
            min_squares = float('inf')
            
            # Try all possible square sizes
            for size in range(min(i, j), 0, -1):
                if i >= size and j >= size:
                    min_squares = min(min_squares, dp[i-size][j-size] + 1)
            
            dp[i][j] = min_squares
    
    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())

print(minSquares(n, m))
