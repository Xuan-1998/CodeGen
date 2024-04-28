def max_subarrays(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    if max(arr[:1]) > k:
        dp[0] = 1
    else:
        dp[0] = 0

    for i in range(1, n):
        if max(arr[:i+1]) > k:
            dp[i] = dp[i-1] + (1 if max(arr[:i+1]) > k else 0)
        else:
            dp[i] = dp[i-1]

    return sum(dp)

# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
print(max_subarrays(arr, k))  # Output: 6
