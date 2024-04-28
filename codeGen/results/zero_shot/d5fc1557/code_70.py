def longestSubarray(nums):
    n = len(nums)
    ans = 0
    left, right = -1, 0
    
    while right < n:
        if nums[right] == 0:
            if left + 1 != right:
                ans = max(ans, right - left)
            left = right
        right += 1
        
    return ans
