def longest_subarray(nums):
    n = len(nums)
    dp = [0] * n
    max_len = 0

    for i in range(1, n):
        if nums[i] == 1:
            dp[i] = dp[i-1] + (nums[i-1] == 1)
            max_len = max(max_len, dp[i])
        else:
            dp[i] = max(dp[i-1], 0)

    return max_len

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(longest_subarray(nums))
