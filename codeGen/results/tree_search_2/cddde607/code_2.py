import sys

def count_paths(K, N, arr):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Base case: count the number of ways to collect exactly K coins from cells (0, 0) to (N-1, N-1)
    dp[N-1][N-1] = sum(1 for i in range(N) for j in range(N) if arr[i][j] == K)

    # Fill up the DP table
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if i < N-1 and j < N-1:
                dp[i][j] = sum(1 for x in range(i+1) for y in range(j+1) if arr[x][y] <= K)
                if arr[i][j] <= K:
                    dp[i][j] += dp[i+1][j] + dp[i][j+1]
            elif i < N-1:
                dp[i][j] = dp[i+1][j]
            elif j < N-1:
                dp[i][j] = dp[i][j+1]

    return dp[0][0]

# Read input from stdin
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(count_paths(K, N, arr))
