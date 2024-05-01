def has_divisible_subset(n, m, nums):
    memo = {}

    def dfs(i):
        if i in memo:
            return memo[i]
        if n == 0:
            return False
        if i >= len(nums) or nums[i] % m != 0:
            result = dfs(i - 1)
        else:
            result = any(dfs(j) for j in range(i)) or (i > 0 and dfs(i - 1))
        memo[i] = result
        return result

    return dfs(len(nums) - 1)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(1 if has_divisible_subset(n, m, nums) else 0)
