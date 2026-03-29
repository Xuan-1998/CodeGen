import sys

def longest_increasing_subsequence(sequence):
    n = len(sequence)
    dp = [1] * n  # Initialize the DP array with all ones, representing single elements as increasing subsequences of length 1.
    
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update the longest increasing subsequence ending at index i.

    return max(dp)

# Read input from standard input.
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.read().split()))

print(longest_increasing_subsequence(sequence))
