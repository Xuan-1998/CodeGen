def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [[-1] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i+1, n)+1):
            if arr[i-1] > arr[i-j]:
                dp[i][j] = max(dp[i-1][j-1], dp[i-j][j]) + 1
            else:
                dp[i][j] = dp[i-1][j]
    return max(max(row) for row in dp)

# Read input from stdin
arr = [int(x) for x in input().split()]

# Print the answer to stdout
print(longest_increasing_subsequences(arr))
