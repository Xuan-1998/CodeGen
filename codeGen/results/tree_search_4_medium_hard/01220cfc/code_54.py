def can_jump(nums):
    memo = {}

    def dfs(index):
        if index == len(nums) - 1:
            return True
        if index in memo:
            return memo[index]
        
        reachable = False
        for i in range(index + 1, min(index + nums[index] + 1, len(nums))):
            if dfs(i):
                reachable = True
                break
        
        memo[index] = reachable
        return reachable

    return dfs(0)
