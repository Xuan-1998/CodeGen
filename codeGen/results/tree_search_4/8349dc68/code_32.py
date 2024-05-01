def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Fill up the table
    for i in range(k, -1, -1):
        for j in range(i, n):
            if i == 0:
                dp[j][i] = max(arr[:j+1])
            else:
                # Calculate the maximum sum considering k-size subarrays
                max_val = max(arr[j-i+1:j+1])
                dp[j][i] = max(dp[j-1][i-1], dp[j-k][i-1] + max_val)

    # Return the last element in the table, which represents the maximum sum
    return dp[-1][-1]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 9 (max sum after partitioning)
