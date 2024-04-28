from bisect import bisect_left
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = max(dp[i], nums[i])
    idx = bisect_left(nums, nums[i] - k)
    for j in range(idx, min(i + 1, len(nums))):
        dp[i + 1] = max(dp[i + 1], dp[j] + nums[i])

print(max(dp))
