from collections import Counter
import sys

def max_points(n, sequence):
    frequency = Counter(sequence)
    max_element = max(sequence)
    dp = [0] * (max_element + 1)

    for i in range(1, max_element + 1):
        take = frequency[i] * i + (dp[i - 2] if i > 1 else 0)
        dont_take = dp[i - 1]
        dp[i] = max(take, dont_take)

    return dp[max_element]

# Reading input from stdin
n = int(input().strip())
sequence = list(map(int, input().strip().split()))

# Calculating and printing the result
print(max_points(n, sequence))
