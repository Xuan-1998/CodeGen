import sys

def longest_increasing_subsequence():
    n = int(input())
    A = list(map(int, input().split()))
    dp = [1] * n  # Initialize the dynamic programming array
    
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j]:  # Check if A[i] is greater than A[j]
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)  # Return the maximum length found

print(longest_increasing_subsequence())
