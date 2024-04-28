def subset_sum_divisible(n, m):
    cumulative_sums = [0] * (m + 1)
    total_sum = 0

    for _ in range(n):
        x = int(input())  # read next number from input
        total_sum += x
        for i in range(m - 1, 0, -1):
            cumulative_sums[i] = cumulative_sums.get(i, 0) + x
            if cumulative_sums[i] % m == 0:
                return 1

    if total_sum % m == 0:  # check the total sum
        return 1

    return 0
