import sys

def longest_increasing_subsequence(array):
    n = len(array)
    dp = [1] * n  # Initialize DP table with ones (shortest subsequences)

    for i in range(n):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
array = [int(x) for x in input().split()]

# Calculate and print the result
print(longest_increasing_subsequence(array))
