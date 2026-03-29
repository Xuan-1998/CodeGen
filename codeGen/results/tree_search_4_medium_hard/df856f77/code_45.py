def min_operations(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    lis_length = 1

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
            if dp[i] > lis_length:
                lis_length = dp[i]
        else:
            if i > 0 and dp[i-1] == dp[i-2]:
                dp[i] = dp[i-2] + 1
            elif i > 1 and arr[i-1] < arr[i-2]:
                dp[i] = dp[i-1] + 1

    return n - lis_length
