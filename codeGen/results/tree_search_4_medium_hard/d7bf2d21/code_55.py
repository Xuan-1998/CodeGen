import sys

def count_longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if arr[j - 1] > arr[j - 2]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
            else:
                dp[i][j] = dp[i-1][j]
        for k in range(i, n + 1):
            if dp[k][n] > 0:
                longest_increasing_subsequences += 1

    return longest_increasing_subsequences


# Read the input array from stdin
arr = list(map(int, sys.stdin.readline().strip().split()))

# Count the number of longest increasing subsequences
longest_increasing_subsequences = count_longest_increasing_subsequences(arr)

# Print the result to stdout
print(longest_increasing_subsequences)
