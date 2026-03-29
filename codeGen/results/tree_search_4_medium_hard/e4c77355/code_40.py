def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp with base case

    for i in range(1, n):
        max_val = 0
        max_length = 0
        for j in range(i):
            if arr[j] < arr[i]:
                val = dp[j]
                if val > max_length:
                    max_length = val + 1
                    max_val = arr[i]
        dp[i] = max_length

    return max(dp)
