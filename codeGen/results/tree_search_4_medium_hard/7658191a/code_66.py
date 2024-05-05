def max_score(n, k, z, array):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: Initialize the first row of the DP table
    for j in range(k + 1):
        dp[0][j] = sum(array[:j])

    # Fill in the DP table
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j > 0:
                right_move = max(dp[i - 1][j - 1] + array[i], dp[i - 1][j])
                left_move = max(dp[i - 1][j - 1] - array[i - 1], dp[i - 1][j])
                dp[i][j] = max(right_move, left_move)
            else:
                dp[i][j] = sum(array[:i])

    return dp[n][k]

# Example usage
n, k, z = map(int, input().split())
array = list(map(int, input().split()))
print(max_score(n, k, z, array))
