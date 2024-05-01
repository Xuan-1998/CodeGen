def find_distinct_sums(nums):
    nums.sort()
    dp = {0: set()}
    achievable = {i: False for i in range(sum(nums) + 1)}
    achievable[0] = True

    for num in nums:
        for sum_val, subsets in list(dp.items()):
            if achievable[sum_val]:
                for subset in subsets:
                    dp.setdefault(sum_val + num, set()).add(frozenset(subset | {num}))
                achievable[sum_val + num] = True
        dp.pop(0)

    return [' '.join(map(str, s)) for s in sorted(dp.values())]

# Test the function
nums = [int(i) for i in input().split()]
print(' '.join(find_distinct_sums(nums)))
