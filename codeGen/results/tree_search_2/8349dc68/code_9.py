def max_sum(arr, k):
    n = len(arr)
    memo = {}

    def dp(i):
        if i >= n:
            return 0
        if (i,) in memo:
            return memo[(i,)]

        max_sum_i = -float('inf')
        for j in range(max(0, i-k+1), i+1):
            max_sum_i = max(max_sum_i, dp(j-1) + max(arr[j:i+1]))

        memo[(i,)] = max_sum_i
        return max_sum_i

    return dp(n-1)

# Example usage:
arr = [3, 2, -2, 3]
k = 3
print(max_sum(arr, k))  # Output: 8
