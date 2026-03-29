def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [[0] * (max(arr) + 1) for _ in range(n)]

    for i, x in enumerate(arr):
        for j in range(x, -1, -1):
            if j == x:
                dp[i][x] = 1
            else:
                dp[i][x] = max(dp[j-1][y] + 1 for y in range(y+1) if arr[y] < x and y >= 0)

    return sum(1 for x in set(max(row) for row in dp) if row.count(x) == n)
