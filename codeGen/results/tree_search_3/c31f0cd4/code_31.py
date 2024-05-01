from functools import lru_cache

@lru_cache(None)
def subset_sums(nums):
    @lru_cache(None)
    def helper(i, remaining_elements):
        if not remaining_elements:
            return 0
        result = []
        for j in range(len(remaining_elements)):
            subset_sum = helper(i + 1, remaining_elements[:j] + remaining_elements[j + 1:])
            result.append(subset_sum + nums[i])
        return sorted(set(result))

    return helper(0, list(range(len(nums))))

n = int(input())
nums = [int(x) for x in input().split()]
print(" ".join(map(str, subset_sums(nums))))
