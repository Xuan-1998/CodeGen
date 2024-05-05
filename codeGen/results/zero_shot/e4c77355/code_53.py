import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dynamic programming array
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

# Read input from standard input
arr = [int(x) for x in sys.stdin.readline().split()]

# Calculate the length of the longest increasing subsequence
length = longest_increasing_subsequence(arr)

# Print the result to standard output
print(length)
