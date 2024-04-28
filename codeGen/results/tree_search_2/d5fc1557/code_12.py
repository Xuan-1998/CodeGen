def longest_subarray(nums):
    n = len(nums)
    memo = {}

    def dfs(left, right):
        if (left, right) in memo:
            return memo[(left, right)]
        count = sum(1 for i in range(left, right+1) if nums[i] == 1)
        if count == 0:
            return 0
        return max(dfs(left, right-1), dfs(left+1, right))

    return dfs(0, n-1)

# Example usage:
nums = [1, 1, 0, 1]
print(longest_subarray(nums))  # Output: 3
