def is_subset_sum_divisible(nums):
    n = len(nums)
    m = int(input())  # read m from input

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # base case: empty set, sum is divisible by 0

    for i in range(1, n + 1):
        for k in range(m + 1):
            if nums[i - 1] % m == 0:
                dp[i][k] = min(dp[i - 1][k], dp[i - 1][k // m] + 1)
            else:
                dp[i][k] = min(dp[i - 1][k], dp[i - 1][min(k, (nums[i - 1] % m) + k // m)] + 1)

    return int(dp[n][0]) == 1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(is_subset_sum_divisible(nums))
