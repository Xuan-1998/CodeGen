import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n):
        max_length = 0
        for j in range(i):
            if arr[i] > arr[j]:
                max_length = max(max_length, dp[j] + 1)
        dp[i + 1] = max_length

    return dp[-1]

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

# Compute the length of the longest increasing subsequence
result = longest_increasing_subsequence(arr)

# Print the result to stdout
print(result)
