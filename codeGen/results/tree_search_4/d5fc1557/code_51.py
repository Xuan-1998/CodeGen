from collections import defaultdict

def longest_ones(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    max_len = 0
    
    for i in range(n-1, -1, -1): # Iterate from right to left
        for j in range(i, n): # Iterate through the array
            if nums[j] == 1:
                dp[i][j] = dp[i+1][j+1] + 2 if i+1 <= j+1 else 0
                max_len = max(max_len, dp[i][j])
    
    return max_len

# Read input from stdin
n = int(input())
nums = [int(x) for x in input().split()]

print(longest_ones(n))
