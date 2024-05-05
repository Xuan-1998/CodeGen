===SOLUTION===
import sys

def longest_increasing_subsequence(sequence):
    n = len(sequence)
    dp = [1] * n  # Initialize dp array with ones.

    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
sequence = [int(x) for x in sys.stdin.readline().split()]

print(longest_increasing_subsequence(sequence))
