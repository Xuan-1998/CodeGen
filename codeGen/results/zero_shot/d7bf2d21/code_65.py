import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n
    max_length = 0

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])

    return max_length

# Read input from standard input
arr = list(map(int, sys.stdin.readline().split()))

# Calculate the number of longest increasing subsequences
result = longest_increasing_subsequences(arr)

# Print the result to standard output
print(result)
