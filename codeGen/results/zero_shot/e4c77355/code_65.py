import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Compute the length of the longest increasing subsequence
result = longest_increasing_subsequence(arr)

# Print the result to stdout
print(result)
