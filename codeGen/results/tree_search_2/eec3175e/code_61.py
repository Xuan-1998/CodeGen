from collections import defaultdict

def min_operations(n, m, arr):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(m + 1):
            if j >= arr[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - arr[i - 1]] + 1)
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
    return 0 if dp[n][m] != float('inf') else -1

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(min_operations(n, m, arr))
