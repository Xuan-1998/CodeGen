def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[1] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i+1, n+1)):
            for k in range(j-1, -1, -1):
                if arr[k] < arr[i]:
                    dp[i][j] = max(dp[i][j], dp[k][j-1]+1)

    return max(max(row) for row in dp)
