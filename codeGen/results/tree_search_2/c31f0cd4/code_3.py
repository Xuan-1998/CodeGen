from functools import lru_cache

def subset_sums(nums):
    @lru_cache(None)
    def dp(i, s):
        if i == 0:
            return [s]
        sums = []
        for j in range(i + 1):
            for x in dp(j, s + nums[j]):
                sums.append(s + nums[i] - sum(x))
        return sorted(list(set(sums)))

    return ' '.join(map(str, set(sum(dp(i, 0)) for i in range(len(nums)))))
