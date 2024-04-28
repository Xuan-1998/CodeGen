import sys

def max_sum_partition(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Initialize the base cases
    for i in range(k + 1):
        dp[0][i] = -sys.maxsize

    # Fill up the DP table
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = max(dp[i-1][j] + arr[i-1], arr[i-1])
            else:
                dp[i][j] = max(dp[i-1][j] + arr[i-1], dp[i-1][j-k] + arr[i-1])

    # Return the maximum sum
    return dp[n][k]


# Read input from standard input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Calculate and print the answer
print(max_sum_partition(arr, k))
