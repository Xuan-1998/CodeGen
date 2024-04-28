n = int(input())
k = int(input())
nums = list(map(int, input().split()))
dp = [0] * (n + 1)
max_sum = float('-inf')
for i in range(1, n):
    if nums[i] - nums[i-1] <= k:
        dp[i] = max(dp[i-1], dp[i-1] + nums[i])
    else:
        dp[i] = dp[i-1]
    max_sum = max(max_sum, dp[i])
print(max_sum)
