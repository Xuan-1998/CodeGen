def maxSubarrayCount(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = max(arr[i-1])
        count = sum(dp[j-1] for j in range(i) if max(arr[j:i+1]) > k)
        dp[i] = count

    return sum(dp)

# Example usage:
arr = [5, 6, 7, 8, 9]
k = 7
print(maxSubarrayCount(arr, k))  # Output: 2
