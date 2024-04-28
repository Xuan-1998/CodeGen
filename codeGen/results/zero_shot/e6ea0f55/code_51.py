nums = list(map(int, input().split()))
k = int(input())
dp = [0] * (len(nums) + 1)
ans = float('-inf')
for i in range(1, len(nums)):
    dp[i] = max(dp[i-1], nums[i] - nums[i-k])
    ans = max(ans, dp[i])
print(ans)
