def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[1] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, n), -1, -1):
            if arr[i - 1] > arr[j - 1]:
                dp[i][j] = max(dp[i][j], dp[j][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

    return max(max(row) for row in dp)

# Read input from stdin
arr = [int(x) for x in input().split()]

print(longest_increasing_subsequence(arr))
