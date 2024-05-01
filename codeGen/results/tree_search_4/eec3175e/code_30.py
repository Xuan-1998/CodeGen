def canPartition(nums, m):
    n = len(nums)
    dp = [False] * (n + 1)

    for i in range(n + 1):
        if i == 0:
            dp[i] = True
        elif nums[i - 1] > m:
            dp[i] = dp[i - 1]
        else:
            dp[i] = any(dp[j] and (nums[i - 1] + sum(nums[j+1:i])) % m == 0 for j in range(i))

    return dp[n]

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(canPartition(nums, m))
