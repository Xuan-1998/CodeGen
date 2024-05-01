def distinct_sums(nums):
    n = len(nums)
    memo = {}
    for i in range(2**n):  # iterate over all possible subsets
        subset_sum = sum([nums[j] for j in range(n) if (i & (1 << j))])
        last_added = bin(i).count('1') - 1  # find the last element added to the subset
        memo[(subset_sum, last_added)] = True

    distinct_sums = sorted(list(memo.keys()))
    return ' '.join(map(str, distinct_sums))
