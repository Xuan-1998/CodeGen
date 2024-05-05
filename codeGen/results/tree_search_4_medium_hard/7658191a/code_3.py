def max_score(array, k):
    n = len(array)
    dp = [[-float('inf')] * (k+1) for _ in range(n+1)]

    # Base cases
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = array[i-1]
            else:
                left_score = -float('inf') if j > z else dp[i-1][j-1]
                right_score = array[i-1] + (dp[i-1][j-1] if i > 1 else 0)
                dp[i][j] = max(left_score, right_score)

    return dp[n][k]

# Example input
array = [5, 3, 2, 8]
k = 2

print(max_score(array, k))  # Output: 14
