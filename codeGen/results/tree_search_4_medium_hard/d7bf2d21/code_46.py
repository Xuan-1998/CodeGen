import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [0] * n
    max_length = 0
    
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    
    count = sum(1 for x in dp if x == max_length)
    return count

# Read input from stdin
arr = [int(x) for x in input().split()]

# Print the answer to stdout
print(longest_increasing_subsequence(arr))
