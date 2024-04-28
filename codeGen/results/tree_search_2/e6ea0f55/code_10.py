def maxSumOfSubsequence(nums, k):
    memo = {}
    
    def dfs(i, diff):
        if (i, diff) in memo:
            return memo[(i, diff)]
        
        if i >= len(nums) or diff < 0:
            return 0
        
        res = max(nums[i] + dfs(i+1, diff-1), nums[i])
        
        memo[(i, diff)] = res
        return res
    
    return max(dfs(0, k), sum(nums))

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    
    print(maxSumOfSubsequence(nums, k))
