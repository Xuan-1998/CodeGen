import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    
    # Initialize dp array with 1s. Since a single-element sequence is always increasing, 
    # the length of the LIS ending at each index is initially 1.
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                # If the current element is greater than the previous element and not previously included 
                # in any increasing subsequence, increment dp[i].
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Read array from stdin
arr = list(map(int, input().split()))

print(longest_increasing_subsequence(arr))
