def longestSubarray(nums):
    n = len(nums)
    ones = 0
    res = 0
    
    memo = {}
    
    for i in range(n):
        if nums[i] == 1:
            ones += 1
        else:
            ones = 0
        
        state = (i, ones)
        
        if state not in memo:
            left = right = i
            while left > 0 and nums[left-1] == 1:
                left -= 1
            while right < n-1 and nums[right+1] == 1:
                right += 1
            
            memo[state] = right - left + 1
        
        res = max(res, memo[state])
    
    return res

def findLongestSubarray(nums):
    n = len(nums)
    if not nums:
        return 0
    
    res = longestSubarray(nums)
    
    # Delete one element
    res -= 1
    
    return max(0, res)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(findLongestSubarray(nums))
