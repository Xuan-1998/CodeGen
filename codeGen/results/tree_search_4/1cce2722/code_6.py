def max_points(sequence):
    n = len(sequence)
    max_value_in_sequence = max(sequence)

    dp = [[0] * (max_value_in_sequence + 1) for _ in range(n)]

    for i in range(1, n):
        for k in range(1, max_value_in_sequence + 1):
            if sequence[i] == k:
                # Delete current element
                delete_current = dp[i - 1][k]
                # Delete subsequent elements
                delete_subsequent = dp[i - 2].get(k - 1, 0) if i > 1 and k - 1 in sequence else 0
                # Choose the maximum option
                dp[i][k] = max(delete_current, delete_subsequent)

    for i in range(n - 2, -1, -1):
        for k in range(1, max_value_in_sequence + 1):
            if sequence[i] == k:
                # Delete current element
                delete_current = dp[i + 1][k]
                # Delete preceding elements
                delete_preceding = dp[i + 2].get(k + 1, 0) if i < n - 2 and k + 1 in sequence else 0
                # Choose the maximum option
                dp[i][k] = max(delete_current, delete_preceding)

    return dp[0][1]
