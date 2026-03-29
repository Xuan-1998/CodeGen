def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # initialize dp array

    max_val = arr[0]
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            dp[i] = dp[i - 1] + 1
        else:
            j = i - 1
            while j >= 0 and arr[j] >= max_val:
                j -= 1
            dp[i] = dp[j + 1] + 1

    return max(dp)
