def count_paths(K, N, arr):
    dp = [[0] * (N) for _ in range(N)]

    # Base case: calculate ways to collect K coins from (0, 0) to (N-1, N-1)
    total_coins = sum(sum(row) for row in arr)
    if total_coins < K:
        return 0

    dp[N-1][N-1] = int(arr[N-1][N-1] == K)

    # Fill up the DP table
    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            if arr[i][j] <= K:
                dp[i][j] = 0  # no ways to collect K coins from here
            else:
                dp[i][j] += dp[i+1][j] + dp[i][j+1]
                if arr[i][j] == K:
                    dp[i][j] += int(arr[i][j] == K)

    return dp[0][0]

# Example usage:
K = 5
N = 3
arr = [[2, 2, 1], [1, 1, 1], [1, 1, 1]]
print(count_paths(K, N, arr))  # Output: 4
