import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp table with ones
    max_length = 1  # Maximum length of any subsequences found

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # Check if it's greater than the previous elements
                dp[i] = max(dp[i], dp[j] + 1)  # Update dp table
        max_length = max(max_length, dp[i])  # Keep track of maximum length

    count = sum(1 for x in dp if x == max_length)  # Count number of longest increasing subsequences
    return count

# Read input from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Print answer to stdout
print(longest_increasing_subsequences(arr))
