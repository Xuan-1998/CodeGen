import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [0] * n
    max_length = 0
    
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    
    return max_length

# Read input from stdin
arr = list(map(int, input().split()))

# Calculate and print the result
print(longest_increasing_subsequence(arr))
