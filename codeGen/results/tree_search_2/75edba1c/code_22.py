def count_subarrays(arr, K):
    n = len(arr)
    dp = [0] * n

    for i in range(1, n):
        if arr[i] > K:
            dp[i] = 1 + (dp[i - 1] if i > 0 else 0)
        elif i > 0 and arr[i] <= K:
            dp[i] = dp[i - 1]

    return sum(dp)

# Example usage
arr = [3, 4, 5, 6, 7]
K = 5
print(count_subarrays(arr, K))  # Output: 3
