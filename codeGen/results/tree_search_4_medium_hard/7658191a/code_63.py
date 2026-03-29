def maximum_score(n, k, z, arr):
    # Initialize the DP table with zeros
    dp = [0] * (k + 1)

    # Calculate the sum of all values in the array
    total_sum = sum(arr)
    dp[0] = total_sum

    for i in range(1, min(k, z) + 1):
        # Consider two cases: last move is right or left
        right_score = arr[i - 1] + dp[i - 1]
        left_score = arr[i - 1] + dp[max(0, i - z - 1)]

        # Choose the maximum score between the two cases
        dp[i] = max(right_score, left_score)

    for i in range(min(k, z) + 1, k + 1):
        # Since we've used all our moves to the left, only right moves are possible
        dp[i] = arr[i - 1] + dp[max(0, i - z - 1)]

    return dp[k]
