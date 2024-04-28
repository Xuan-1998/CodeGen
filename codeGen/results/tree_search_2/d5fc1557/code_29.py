def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    max_length = 0

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
            max_length = max(max_length, dp[i])
        else:
            dp[i] = 0

    return max_length - 1

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_subarray(nums))
