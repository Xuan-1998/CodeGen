import sys

def longest_increasing_subsequence():
    n = int(sys.stdin.readline().strip())
    seq = list(map(int, sys.stdin.readline().strip().split()))
    
    dp = [1] * (n + 1)  # Initialize the dynamic programming array
    
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:  # Check if current element is greater than previous one
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)  # Return the length of the longest increasing subsequence

print(longest_increasing_subsequence())
