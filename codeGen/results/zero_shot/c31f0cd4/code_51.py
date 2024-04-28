n = int(input())
nums = list(map(int, input().split()))
dp = [[[] for _ in range(sum(nums) + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(sum(nums) + 1):
        if j < nums[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = set.union(*[set(dp[k][m] for m in range(m, j + 1)) for k in range(i) if m <= nums[i - 1]])
print(' '.join(map(str, sorted(set.union(*[set(dp[k][m] for m in range(m, sum(nums) + 1)) for k in range(n)])))))
