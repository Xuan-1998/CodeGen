def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = {}

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if i == 0:
                dp[(i, j)] = 0
            elif j == 0:
                dp[(i, j)] = arr[i - 1]
            else:
                dp[(i, j)] = max(dp.get((i - 1, j - 1), 0) + arr[i + j - 1], dp.get((i, k - j - 1), 0))

    return dp.get((n, k), 0)
