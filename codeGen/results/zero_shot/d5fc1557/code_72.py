def longestSubarray(nums):
    n = len(nums)
    ans = 0
    cnt = 0
    
    for i in range(n-1, -1, -1):
        if nums[i] == 0:
            cnt = 0
        else:
            cnt += 1
        ans = max(ans, cnt)
    
    return n - (ans + 1)
