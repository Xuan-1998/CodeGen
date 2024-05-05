import sys

def longest_increasing_subsequence_length(arr):
    n = len(arr)
    
    # Initialize dp array where dp[i][j] represents the length of 
    # the longest increasing subsequence ending at index j in the first i elements.
    dp = [[0] * n for _ in range(n)]
    
    # Step 1: Traverse the input array from left to right
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][j] = dp[j][j] + 1
            else:
                dp[i][j] = dp[j][j]
    
    # Step 2: Traverse the input array from right to left
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                dp[i][j] = min(dp[i][k] for k in range(i+1, j))
    
    # The number of longest increasing subsequences is the sum of all unique values 
    # in dp[][] array.
    max_length = 0
    seen_lengths = set()
    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j]:
                continue
            length = dp[i][j]
            if length not in seen_lengths:
                seen_lengths.add(length)
                max_length += 1
    
    return max_length

# Read the array from standard input.
arr = [int(x) for x in sys.stdin.readline().split()]

print(longest_increasing_subsequence_length(arr))
