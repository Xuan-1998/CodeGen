def distinct_sum_sets(nums):
    nums.sort()
    dp = {}
    def dfs(i, s):
        if (i, s) in dp:
            return dp[(i, s)]
        if s == 0:
            return [0]
        if i >= len(nums) or s > sum(nums):
            return []
        sums = set()
        for k in range(1 + (s // nums[i])):
            remaining_sum = s - k * nums[i]
            subsets = dfs(i-1, remaining_sum)
            for subset_sum in subsets:
                sums.add(k * nums[i] + subset_sum)
        dp[(i, s)] = list(sums)
        return dp[(i, s)]
    result = set()
    for i in range(len(nums) + 1):
        result.update(dfs(i, sum(nums)))
    return sorted(list(result))
