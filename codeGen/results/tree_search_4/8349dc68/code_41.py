def max_sum_after_partitioning(arr, k):
    n = len(arr)
    memo = {}

    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if k > i:
            return max(dp(i-1, k-1) + arr[i], dp(i-1, k))
        else:
            return dp(i-1, k)
        memo[(i, k)] = result
        return result

    return dp(n-1, k)

# Example usage
arr = [3, 2, -1, 5, 6, 0]
k = 2
print(max_sum_after_partitioning(arr, k))  # Output: 10
