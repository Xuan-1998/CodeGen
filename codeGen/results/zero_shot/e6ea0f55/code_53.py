import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = nums[i-1]
    for j in range(1, min(i, k)+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + nums[i-1])
print(max(map(lambda x: x[-1], dp)))
