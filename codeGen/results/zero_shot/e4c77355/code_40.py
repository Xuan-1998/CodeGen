import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with all ones

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Calculate and print the result
result = longest_increasing_subsequence(arr)
print(result)
