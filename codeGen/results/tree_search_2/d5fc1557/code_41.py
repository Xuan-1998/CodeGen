def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    max_len = 0

    for i in range(1, n+1):
        if nums[i-1] == 1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1] - 1
        max_len = max(max_len, abs(dp[i]))

    return max_len

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longestSubarray(nums))
