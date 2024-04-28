import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)
max_sum = float('-inf')
for i in range(1, n):
    dp[i] = max(dp[i-1], nums[i-1])
    if i >= k:
        dp[i] = max(dp[i], dp[i-k]+nums[i])
    else:
        dp[i] = max(dp[i], 0)
max_sum = max(max_sum, dp[-1])
print(max_sum)
