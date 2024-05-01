def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = max(dp[i - 1], i - i) + (nums[i] == 1)
        else:
            dp[i] = dp[i - 1]

    return max(dp)

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_subarray(nums))
