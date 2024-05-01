from functools import lru_cache

def distinct_sum_set(nums):
    @lru_cache(None)
    def dfs(i, total):
        if i == len(nums):
            return [total]
        sums = []
        for j in range(i + 1):
            sums += dfs(j, total + nums[j])
        return sums

    sums = set()
    for i in range(len(nums) + 1):
        sums.update(dfs(i, 0))
    return sorted(list(sums))

N = int(input())
nums = [int(x) for x in input().split()]
print(' '.join(map(str, distinct_sum_set(nums))))
