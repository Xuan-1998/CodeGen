def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[1] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][j] = max(dp[i-1][k] + 1 for k in range(j) if arr[k] < arr[j])

    return max(max(row) for row in dp)
