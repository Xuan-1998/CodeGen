def min_height(n, max_width, thicknesses):
    dp = [[-1 for _ in range(max_width+1)] for _ in range(n+1)]
    
    # Base case: empty bookcase has height 0
    for w in range(max_width+1):
        dp[0][w] = 0
    
    for i in range(1, n+1):
        for w in range(max_width+1):
            if thicknesses[i-1] > w:
                # If the current book doesn't fit on any shelf, 
                # we have to start a new shelf
                dp[i][w] = dp[i-1][0] + thicknesses[i-1]
            else:
                # Try placing the current book on an existing shelf
                for j in range(w):
                    if dp[i-1][j+w-thicknesses[i-1]] != -1:
                        dp[i][w] = min(dp[i][w], dp[i-1][j+w-thicknesses[i-1]] + thicknesses[i-1])
    
    # Return the minimum height of the bookcase after placing all n books
    return dp[n][max_width]
