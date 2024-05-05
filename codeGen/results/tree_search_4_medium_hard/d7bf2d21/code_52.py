import sys
from collections import defaultdict

def longest_increasing_subsequences(array):
    dp = [-sys.maxsize] * len(array)
    max_length = 0
    
    for i in range(len(array)):
        dp[i] = 1
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    
    count_max_length = sum(1 for x in dp if x == max_length)
    return count_max_length

# Read input from stdin
array = [int(x) for x in input().split()]

print(longest_increasing_subsequences(array))
