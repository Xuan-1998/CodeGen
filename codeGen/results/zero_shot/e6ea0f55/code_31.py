n = int(input())
k = int(input())
nums = list(map(int, input().split()))
dp = [0] * (len(nums) + 1)
max_sum = float('-inf')
for i in range(1, len(nums) + 1):
    dp[i] = max(dp[i-1], nums[i-1])
    for j in range(min(i, k), -1, -1):
        dp[i] = max(dp[i], dp[j] + nums[i-1])
print(max_sum)
