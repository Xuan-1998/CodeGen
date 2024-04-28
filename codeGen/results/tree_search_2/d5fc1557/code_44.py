def longest_subarray(nums):
    n = len(nums)
    dp = {i: 0 for i in range(n)}
    
    max_length = 0
    prev_end_index = -1
    
    for i in range(n):
        if nums[i] == 1:
            dp[i] = dp.get(i-1, 0) + 1 if i > 0 else 1
            max_length = max(max_length, dp[i])
            if prev_end_index != -1 and i - dp[prev_end_index] >= max_length:
                return max_length
        else:
            prev_end_index = i
    
    return max_length

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    
    print(longest_subarray(nums))
