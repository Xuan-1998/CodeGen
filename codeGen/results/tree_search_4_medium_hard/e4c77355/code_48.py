def length_of_longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[1] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][j] = max(dp[i][j], dp[j][j-1] + 1)

    return max(max(row) for row in dp)
