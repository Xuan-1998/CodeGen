from collections import defaultdict

def maxSumSubsequence(nums, k):
    dp = defaultdict(int)
    dp[-1][-1] = 0
    
    for i in range(len(nums)):
        for j in range(min(i+1, k+1)):
            if i == 0:
                dp[(i,j)] = nums[i]
            else:
                dp[(i,j)] = max(dp[(i-1,k)] + nums[i] for k in range(0, min(i, j+1)))
    
    return max(dp.values())

# Example usage
nums = [2, 3, -1, 5, -3, 2]
k = 3
print(maxSumSubsequence(nums, k))  # Output: 7
