def maxSum(nums, k):
    n = len(nums)
    dp = {0: 0}

    for i in range(1, n+1):
        if i > k:
            dp[i] = max(dp[j] + nums[i-1] - nums[j-1] for j in range(max(0, i-k), i))
        else:
            dp[i] = max(nums[0], 0)

    return max(dp.values())

nums = list(map(int, input().split()))
k = int(input())
print(maxSum(nums, k))
