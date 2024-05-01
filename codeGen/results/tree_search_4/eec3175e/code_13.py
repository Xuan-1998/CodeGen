from collections import defaultdict

def find_subset(arr, m):
    n = len(arr)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for k in range(1, m+1):
            if arr[i-1] <= k:
                dp[i][k] = (dp[i-1][k-arr[i-1]] or dp[i-1][k]) or dp[i-1][k]
            else:
                dp[i][k] = dp[i-1][k]

    return 1 if dp[n][m] else 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(find_subset(arr, m))
