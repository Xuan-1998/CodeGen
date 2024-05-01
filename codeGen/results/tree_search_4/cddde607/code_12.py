def numPaths(arr, N, K):
    # Create a memoization table to store intermediate results
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # Fill up the memoization table
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= K:
                if i == N-1 and j == N-1:  # Base case: only one path
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0

    return dp[N-1][N-1]

# Read input from stdin
K, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# Calculate and print the result
print(numPaths(arr, N, K))
