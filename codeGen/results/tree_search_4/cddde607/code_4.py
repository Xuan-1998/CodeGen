import sys

def count_paths(K, N, arr):
    # Initialize the dp table with zeros
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # Base cases: Initialize the first row and column
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + arr[0][j]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + arr[i][0]

    # Fill up the rest of the dp table
    for i in range(1, N):
        for j in range(1, N):
            if arr[i-1][j-1] <= K:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                # If the number of coins collected at cell (i, j) is greater than k
                dp[i][j] = 0

    return dp[N-1][N-1]

# Read input from stdin
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(count_paths(K, N, arr))
