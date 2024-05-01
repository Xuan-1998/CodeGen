def num_paths_with_k_coins(K, N, arr):
    # Initialize the memoization table with zeros
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Base case: there is only one way to collect 0 coins (i.e., not move at all)
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= K:
                if i < N-1 and j > 0:
                    dp[i+1][j] += dp[i][j]
                if i > 0 and j < N-1:
                    dp[i][j+1] += dp[i][j]
                if i > 0 and j > 0:
                    dp[i][j] += dp[i-1][j-1]
    
    # Return the number of paths that collect exactly K coins
    return dp[0][0]

# Read input from stdin
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# Print the output to stdout
print(num_paths_with_k_coins(K, N, arr))
