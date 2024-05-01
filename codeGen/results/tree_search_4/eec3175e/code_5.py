def has_subset_sum_divisible_by_m(n, m, nums):
    dp = {(i, j): False for i in range(n+1) for j in range(m)}
    dp[(0, 0)] = True

    for i in range(1, n+1):
        for j in range(m):
            if (j - nums[i-1] % m) * m <= m-1 and dp[(i-1, ((j - nums[i-1] % m) * m) % m)]:
                dp[(i, j)] = True

    return 1 if any(dp[(n, j)]) for j in range(m)] else 0
