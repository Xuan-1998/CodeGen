import sys

def find_sums(nums):
    memo = {}
    max_sum = sum(nums)

    def dp(subset, total):
        if (subset, total) in memo:
            return memo[(subset, total)]

        res = False
        for i, num in enumerate(nums):
            if subset & (1 << i):
                new_subset = subset ^ (1 << i)
                res |= dp(new_subset, total - num)

        memo[(subset, total)] = res
        return res

    result = []
    for sum_val in range(max_sum + 1):
        if dp(0, sum_val):
            result.append(str(sum_val))

    print(' '.join(sorted(result)))

N = int(input())
nums = list(map(int, input().split()))
find_sums(nums)
