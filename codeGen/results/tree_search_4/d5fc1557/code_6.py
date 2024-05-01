def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if nums[i-1] == 1:
            if i > 1 and nums[i-2] == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
    
    return max(dp) - 1

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    
    print(longest_subarray(nums))
