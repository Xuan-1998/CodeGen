import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    max_length = 0
    count_max_length = 0
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if arr[j - 1] > arr[j - 2]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i-1][j]
            
            max_length = max(max_length, dp[i][j])
    
    for i in range(1, n + 1):
        count_max_length += sum(x == max_length for x in dp[i][:n+1])
    
    return count_max_length

# Example usage:
arr = [3, 4, 2, 5, 1]
print(longest_increasing_subsequences(arr))  # Output: 2
