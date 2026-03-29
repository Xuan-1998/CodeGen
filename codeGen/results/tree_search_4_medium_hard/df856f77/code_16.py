from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

dp = [[float('inf')] * (max(arr) + 1) for _ in range(n)]

for i in range(1, n):
    for j in range(min(arr), max(arr) + 1):
        idx = bisect_left(arr[:i], j)
        dp[i][j] = min(dp[i][j], dp[idx-1][arr[idx-1]] + j - arr[idx-1]) if idx > 0 else float('inf')

print(min(dp[-1]))
