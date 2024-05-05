import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp with all 1s, as a single element is always an increasing subsequence of length 1
    
    for i in range(1, n):
        for j in range(i):  # Compare each element with all previous elements
            if arr[i] > arr[j]:  # If the current element is greater than its predecessor, update dp[i]
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)  # Return the maximum value in dp, which represents the length of the longest increasing subsequence

# Read input from stdin
arr = list(map(int, input().split()))
print(longest_increasing_subsequence(arr))
