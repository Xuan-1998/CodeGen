import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    
    # Initialize memoization dictionary
    dp = {i: 0 for i in range(n + 1)}
    
    for i in range(1, n + 1):
        for j in range(i - k, -1, -1):
            if i <= j + k:
                dp[i] = max(dp[i], max_sum_subarray(arr[j:i]))
            
    return dp[n]

def max_sum_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Read inputs from stdin
n, k = map(int, input().split())
arr = [int(x) for x in input().split()]

# Calculate and print the result
print(max_sum_after_partitioning(arr, k))
