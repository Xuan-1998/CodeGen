def can_partition(arr):
    arr.sort()
    n, k, m = len(arr), 0, 0

    dp = [[False] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if i < k:
                dp[i][j] = True
            elif j > 0 and (arr[i - 1] - arr[0] <= m or not dp[i - k][j - 1]):
                dp[i][j] = True

    return dp[n][k]

n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_partition(arr))
