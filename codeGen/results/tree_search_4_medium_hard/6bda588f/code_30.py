def min_function_value(a, s):
    n = len(a)
    dp = [[float('inf')] * (s + 1) for _ in range(n + 1)]

    # Base case: when there are no more numbers left to consider
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(s + 1):
            # Include the current number in the sum
            include_current_number = max(0, a[i - 1] - s) if i > 1 else float('inf')
            dp[i][j] = min(dp[i - 1][a[i - 1] - s] + include_current_number, dp[i - 1][j])

    # The final answer is the minimum of the states when we've processed all numbers
    return min(dp[n])
