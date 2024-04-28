n, k = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    max_sum = 0
    for j in range(max(0, i-k), min(i+1, k)):
        if dp[j] > 0:
            max_sum = max(max_sum, dp[j] + nums[i])
    dp[i] = max_sum

print(dp[-1])  # Print the maximum sum of a subsequence
