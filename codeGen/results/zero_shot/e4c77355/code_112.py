import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Read input
arr = list(map(int, input().split()))

# Calculate the length of the longest increasing subsequence
lis_length = longest_increasing_subsequence(arr)

print(lis_length)
