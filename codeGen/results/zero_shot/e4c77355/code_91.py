from sys import stdin

def longest_increasing_subsequence():
    # Read input array
    arr = [int(x) for x in stdin.readline().split()]
    
    # Initialize dynamic programming table (dp)
    n = len(arr)
    dp = [[1] * n for _ in range(n)]
    
    # Fill up the dp table
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                dp[i][j] = max(dp[i][j], dp[i][j - 1][j - 1] + 1) if j > 0 else 2
            else:
                dp[i][j] = dp[i][j - 1][j]
    
    # Return the maximum length of increasing subsequence
    return max(max(row) for row in dp)

print(longest_increasing_subsequence())
