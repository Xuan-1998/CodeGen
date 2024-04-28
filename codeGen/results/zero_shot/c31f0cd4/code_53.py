from collections import defaultdict
n = int(input())
nums = list(map(int, input().split()))
dp = [defaultdict(int)] + [{0: 1} for _ in range(n)]
for i in range(1, n+1):
    for j in range(sum(nums), -1, -1):
        if j >= nums[i-1]:
            dp[i][j] += dp[i-1].get(j-nums[i-1], 0)
sums = sorted(set(sum(subset) for subset in (tuple(dp[i]) for i in range(1, n+1))))
print(*sums, sep=' ')
