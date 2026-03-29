def min_operations(arr):
    n = len(arr)
    dp = [float('inf')] * (n + 1)

    # Base cases
    dp[0] = 0
    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            dp[i] = 1
        else:
            dp[i] = min(dp[i - 1], 1 + (i > 1 and arr[i - 2] < arr[i]))

    # Return the minimum number of operations required to make the array strictly increasing
    return dp[-1]
