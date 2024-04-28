def longestSubarray(nums):
    n = len(nums)
    dp = {0: 0}
    max_len = 0
    
    for i in range(n):
        if nums[i] == 1:
            new_state = i + 1
        else:
            new_state = 0
        
        for prev_state in list(dp.keys()):
            new_state += 1
            dp[new_state] = max(dp.get(new_state, 0), dp[prev_state])
        
        if new_state not in dp:
            dp[new_state] = 0
        
        max_len = max(max_len, dp[new_state])
    
    return n - 1 - max_len

input()
n = int(input())
nums = [int(x) for x in input().split()]
print(longestSubarray(nums))
