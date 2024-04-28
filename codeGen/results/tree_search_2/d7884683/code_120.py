def max_partition_count(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i == 0:  # base case: one-element array
            dp[i] = 1
        elif i == 1:  # base case: two-element array
            dp[i] = int(arr[0] == arr[1])
        else:
            left_sum = sum(arr[:i-1])
            right_sum = sum(arr[i:])
            if left_sum == right_sum:  # partition at index i
                dp[i] = max(dp[i-1], dp[i-2] + 1)
            else:  # don't partition at index i
                dp[i] = dp[i-1]

    return dp[-1]
