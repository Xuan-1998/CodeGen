def find_sums(nums):
    n = len(nums)
    max_sum = sum(nums)
    dp = [[[] for _ in range(max_sum + 1)] for _ in range(n + 1)]

    def dfs(i, j, subset):
        if i > n:
            return [j]
        if j <= 0:
            return []
        if dp[i][j]:
            return dp[i][j]
        
        subset = set(subset)
        include = dfs(i + 1, j - nums[i], subset | {nums[i]})
        exclude = dfs(i + 1, j, subset)
        dp[i][j] = [x for x in (include[0],) if x not in exclude]
        return dp[i][j]

    sums = set()
    dfs(0, max_sum, set())
    return ' '.join(map(str, sorted(sums)))
