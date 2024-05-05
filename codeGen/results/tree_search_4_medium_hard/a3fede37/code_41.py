def max_sum_of_path(nums):
    n = len(nums)
    memo = [[0] * (n + 1) for _ in range(n + 1)]
    
    def dfs(i, j):
        if i == j:
            return nums[i]
        if memo[i][j]:
            return memo[i][j]
        
        max_sum = float('-inf')
        for k in range(i, j + 1):
            left_sum = dfs(i, k - 1) if i > 0 else 0
            right_sum = dfs(k + 1, j) if k < n - 1 else 0
            max_sum = max(max_sum, nums[k] + left_sum + right_sum)
        
        memo[i][j] = max_sum
        return max_sum
    
    return max(dfs(0, n - 1), key=lambda x: x[1])

# Example usage:
nums = [1, 2, 3, None, 4, 5, None, None]
print(max_sum_of_path(nums))
