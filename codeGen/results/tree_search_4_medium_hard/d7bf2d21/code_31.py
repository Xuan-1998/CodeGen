import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP array with values initialized to 1
    max_length = 1  # Keep track of the maximum length seen so far
    
    for i in range(1, n):  # Iterate through the array from left to right
        for j in range(i):
            if arr[i] > arr[j]:  # If the current element is greater than the previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update the DP array based on the previously processed elements
        if dp[i] > max_length:  # If we've seen a longer increasing subsequence, update the maximum length
            max_length = dp[i]
    
    count = 0  # Initialize the count of longest increasing subsequences to 0
    for i in range(n):
        if dp[i] == max_length:  # Count the number of times the maximum length is reached
            count += 1
    
    return count

# Example usage:
arr = list(map(int, input().split()))
print(longest_increasing_subsequences(arr))
