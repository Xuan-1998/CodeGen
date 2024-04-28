def min_squares(n, m):
    # Initialize a DP table with size (n+1) x (m+1)
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    # Base case: 0x0 rectangle requires 0 squares
    dp[0][0] = 0
    
    # Fill the DP table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_squares = float('inf')
            
            # Try all possible square side lengths
            for k in range(min(i, j), 0, -1):
                if (i >= k and j >= k) or (i < k and j < k):
                    min_squares = min(min_squares, dp[i-k][j-k] + 1)
            
            # Update the DP table with the minimum number of squares
            dp[i][j] = min_squares
    
    return dp[n][m]

# Example usage:
n, m = map(int, input().split())
print(min_squares(n, m))
