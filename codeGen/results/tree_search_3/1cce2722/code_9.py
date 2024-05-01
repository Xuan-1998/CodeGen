def max_points(n, sequence):
    # Initialize the dp array with zeros
    dp = [0] * (n + 1)

    # Base case: when there are no more elements left to delete
    dp[0] = 0

    for i in range(1, n + 1):
        if sequence[i - 1] % 2 == 1:
            # If the current element is odd, consider deleting it along with its neighbors
            dp[i] = max(dp[i - 1], dp[i - 2] + (i >= 3) * 2)
        else:
            # If the current element is even, only consider not deleting it
            dp[i] = dp[i - 1]

    return dp[n]
