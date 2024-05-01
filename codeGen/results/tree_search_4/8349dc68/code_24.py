def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    memo = {0: 0}

    for i in range(1, n + 1):
        if i < k:
            memo[i] = max(memo[i - 1], arr[i - 1])
        else:
            memo[i] = max(memo[i - k], arr[i - 1]) + arr[i - 1]

    return memo[n]
