nums = list(map(int, input().split()))
k = int(input())
dp = [0] * (len(nums) + 1)
max_sum = float('-inf')
for i in range(len(nums)):
    dp[i + 1] = max(dp[i], nums[i])
    for j in range(i - k, i):
        if j >= 0:
            dp[i + 1] = max(dp[i + 1], dp[j] + nums[i])
print(max_sum)
