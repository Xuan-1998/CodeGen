def longest_ones(nums):
    n = len(nums)
    memo = {}
    
    def helper(i):
        if i in memo:
            return memo[i]
        
        if i >= n or nums[i] == 0:
            return 0
        
        result = 1
        if i > 0 and nums[i-1] == 1:
            result = max(result, helper(i-1))
        
        memo[i] = result
        return result
    
    return max(helper(i) for i in range(n))

# Test the function
n = int(input())
nums = [int(x) for x in input().split()]
print(longest_ones(nums))
