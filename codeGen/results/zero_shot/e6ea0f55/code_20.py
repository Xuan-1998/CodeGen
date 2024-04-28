from collections import defaultdict

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)
    prev = defaultdict(int)

    for i in range(n - 1, -1, -1):
        curr_sum = nums[i]
        for j in range(i - 1, max(0, i - k - 1), -1):
            curr_sum += nums[j]
            dp[i] = max(dp[i], curr_sum)
            prev[dp[i]] = min(prev.get(dp[i], i + 1), j)

    return dp[0]

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(maxSumSubsequence(nums, k))
