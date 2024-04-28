def longestSubarray(nums):
    n = len(nums)
    if not nums:
        return 0
    
    max_length = 0
    left = 0
    for right in range(n):
        while left <= right and (left == 0 or nums[left - 1] != nums[right]):
            left += 1
        max_length = max(max_length, right - left + 1)
    
    return max_length

n = int(input())
nums = list(map(int, input().split()))
print(longestSubarray(nums))
