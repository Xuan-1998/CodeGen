def count_paths_k_coins(K, N, arr):
    dp = [[0] * (N+1) for _ in range(N+1)]

    # Base case: top-left cell
    if arr[0][0] <= K:
        dp[0][0] = 1

    # Fill up the DP table
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i-1][j-1] <= K:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0

    return dp[N-1][N-1]

# Example usage
K, N = map(int, input().split())
arr = [[int(x) for x in line.split()] for line in [input() for _ in range(N)]]
print(count_paths_k_coins(K, N, arr))
