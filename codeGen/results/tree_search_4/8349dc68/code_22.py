import sys

def solve(arr, k):
    n = len(arr)
    if k > n:
        return 0
    dp = [[0] * (k+1) for _ in range(n+1)]
    max_val = max(arr)
    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            prev_max = max(dp[i-1][j-1], 0) if j > 0 else 0
            dp[i][j] = max(dp[i-1][j-1] + max_val, dp[i-1][j])
    return max([dp[i][k] for i in range(n-k+1)])

# Read input from stdin
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(solve(arr, k))
