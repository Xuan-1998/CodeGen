def min_squares(n, m):
    # Initialize dp array with base cases
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base cases: empty rectangles require no squares
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0
    
    # Calculate minimum number of squares required to tile sub-rectangles
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < j:
                dp[i][j] = min(dp[i - k][j - l] + 1 for k in range(i + 1) for l in range(j + 1))
            else:
                dp[i][j] = min(dp[i - k][j] + 1 for k in range(1, i + 1))
    
    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())

# Print the minimum number of squares required to tile the rectangle
print(min_squares(n, m))
