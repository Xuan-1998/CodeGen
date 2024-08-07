import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize table with all elements set to 1
    
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    max_length = max(dp)
    count = sum(1 for x in dp if x == max_length)
    
    return count

# Read input from stdin
arr = list(map(int, input().split()))

# Print the answer to stdout
print(longest_increasing_subsequences(arr))
