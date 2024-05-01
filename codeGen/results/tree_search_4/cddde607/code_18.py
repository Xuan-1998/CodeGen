def count_paths(arr, K):
    N = len(arr)
    
    # Create a 2D table to store intermediate results
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Fill up the table dp[][] in a bottom-up manner
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i-1][j-1] <= K:
                if i == 1 and j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Return the number of paths that collect exactly K coins from the top left corner
    return dp[1][1]

# Example usage:
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(count_paths(arr, K))
