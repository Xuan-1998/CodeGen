import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    max_length = 1

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])

    return max_length

# Read input from stdin
arr = [int(x) for x in input().split()]

# Calculate the length of the longest increasing subsequence
max_lis_length = longest_increasing_subsequence(arr)

# Print the result to stdout
print(max_lis_length)
