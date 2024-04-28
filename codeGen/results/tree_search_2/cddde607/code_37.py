def count_paths(K, N, arr):
    dp = [[0]*N for _ in range(N)]
    
    # Base case
    if arr[0][0] <= K:
        dp[0][0] = 1
    
    # Fill up the DP table
    for i in range(1, N):
        for j in range(1, N):
            if arr[i][j] <= K:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[N-1][N-1]

# Example usage
K = int(input())  # Read K from stdin
N = int(input())  # Read N from stdin
arr = [[int(x) for x in input().split()] for _ in range(N)]  # Read the 2D array from stdin

result = count_paths(K, N, arr)
print(result)  # Print the result to stdout
