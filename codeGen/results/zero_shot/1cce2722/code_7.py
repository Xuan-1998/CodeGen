from collections import Counter
import sys

def max_points(sequence):
    freq = Counter(sequence)
    max_num = max(sequence)
    dp = [0] * (max_num + 1)
    dp[1] = freq[1] * 1

    for i in range(2, max_num + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * freq[i])

    return dp[max_num]

# Read input from stdin
n = int(input().strip())
sequence = list(map(int, input().strip().split()))

# Calculate and print the maximum number of points
print(max_points(sequence))
