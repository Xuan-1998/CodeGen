from bisect import bisect_left
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
max_sum = [0] * len(nums)
for i in range(1, len(nums)):
    max_sum[i] = max_sum[i-1] + nums[i]
for gap in range(k+1):
    for i in range(gap+1):
        j = bisect_left(nums[:i], nums[i]-gap, 0, i)
        if j < i:
            dp[gap][j] = max(dp[gap][j-1], max_sum[j-1] - max_sum[i-1] + nums[i])
print(max(dp[k]))
