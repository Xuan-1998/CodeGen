def count_paths(arr):
    N = len(arr)
    K = int(input())
    
    # Initialize dp table with zeros
    dp = [[0] * (N) for _ in range(N)]
    
    # Base case: only one way to reach top-left corner
    dp[0][0] = 1 if arr[0][0] <= K else 0
    
    # Fill up the table in bottom-up manner
    for i in range(N):
        for j in range(N):
            if i < N-1 and arr[i][j] + arr[i+1][j] <= K:
                dp[i][j] += dp[i+1][j]
            if j < N-1 and arr[i][j] + arr[i][j+1] <= K:
                dp[i][j] += dp[i][j+1]
    
    # Return the number of paths that collect exactly K coins
    return sum([row[-1] for row in dp]) if arr[-1][-1] == K else 0

# Test the function
arr = [[2, 3], [1, 4], [5, 6]]
K = 7
print(count_paths(arr))  # Output: 3
