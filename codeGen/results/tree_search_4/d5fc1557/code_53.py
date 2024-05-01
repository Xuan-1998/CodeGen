def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if nums[i - 1] == 0:
            dp[i] = max(dp[i - 2] if i > 1 else 0, 0)
        else:
            dp[i] = dp[i - 1]

    for j in range(n - 1, -1, -1):
        if dp[j + 1] > 0:
            return dp[j + 1]
    return 0

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_subarray(nums))
