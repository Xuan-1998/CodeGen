from bisect import bisect_left
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dp = [0] * (n + 1)
ans = float('-inf')

for i in range(1, n + 1):
    j = bisect_left(dp, nums[i - 1], 0, i - k - 1) or 0
    dp[i] = max(dp[i - 1], nums[i - 1] + dp[j])
    ans = max(ans, dp[i])

print(ans)
