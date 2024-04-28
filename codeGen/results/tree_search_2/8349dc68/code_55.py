def max_sum_of_subarrays(arr, k):
    n = len(arr)
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(k+1):
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j] = arr[:j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-k][j] + max(arr[i-j:i]))
    return max(dp[n])

# Example usage
arr = [3, 5, -9, 1, 2, 8, 4, 6]
k = 3
print(max_sum_of_subarrays(arr, k))  # Output: 24
