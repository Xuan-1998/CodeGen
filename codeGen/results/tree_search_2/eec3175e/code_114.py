def subset_sum_divisible(n, m, arr):
    dp = {}

    for i in range(1, n + 1):
        for j in range(m):
            if j == 0:
                dp[(i, j)] = True
            elif j < i:
                dp[(i, j)] = False
            else:
                dp[(i, j)] = dp.get((i - 1, j), False) or (j >= arr[i-1] and dp.get((i - 1, j - arr[i-1]), False))

    return dp.get((n, m - 1), False)
