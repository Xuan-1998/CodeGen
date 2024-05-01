def distinct_sums(nums):
    max_sum = sum(nums)
    dp = set()
    for i in range(1 << len(nums)):
        subset_sum = 0
        for j in range(len(nums)):
            if (i & (1 << j)) > 0:
                subset_sum += nums[j]
        dp.add(subset_sum)

    result = []
    for sum_val in range(max_sum + 1):
        if sum_val in dp:
            result.append(str(sum_val))

    return ' '.join(sorted(result))

print(distinct_sums([1, 2, 3]))
