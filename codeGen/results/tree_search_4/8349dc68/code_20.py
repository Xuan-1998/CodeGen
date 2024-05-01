def max_sum_after_partitioning(arr, k):
    n = len(arr)
    memo = {}

    def f(i, prev_max):
        if (i, prev_max) in memo:
            return memo[(i, prev_max)]
        
        max_value = max(arr[i-k:i])
        if i <= k:
            res = max_value
        else:
            res = max_value + f(i-k, max_value)
        memo[(i, prev_max)] = res
        return res

    for j in range(1, k+2):
        for i in range(j, n+1):
            memo[(i-j, j)] = f(i-1, memo.get((i-k-1, k), 0))

    return max(memo.values())
