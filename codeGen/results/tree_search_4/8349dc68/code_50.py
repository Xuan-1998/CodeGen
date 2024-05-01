def max_sum_after_partitioning(arr, k):
    n = len(arr)
    memo = {}

    def dp(i):
        if i >= n:
            return 0
        if (i,) in memo:
            return memo[(i,)]
        
        if i + k > n:
            max_sum = max(arr[i:])
            return max_sum

        max_sum = arr[i]
        for j in range(i, min(n, i+k)):
            max_sum = max(max_sum, dp(j) + arr[j])

        memo[(i,)] = max_sum
        return max_sum

    max_val = float('-inf')
    max_sum = 0
    for i in range(0, n, k):
        if i + k > n:
            break
        val = dp(i)
        max_sum += val
        max_val = max(max_val, val)

    return max_sum
