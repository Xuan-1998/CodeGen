import sys

def longest_increasing_subsequence(array):
    n = len(array)
    
    # dp[i] will store the length of LIS ending at index i.
    dp = [1]*n

    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j]+1)
                
    # Return the maximum value from the dynamic programming array
    return max(dp)

# Read input from stdin
input_array = list(map(int, input().split()))

# Calculate and print the length of LIS
print(longest_increasing_subsequence(input_array))
