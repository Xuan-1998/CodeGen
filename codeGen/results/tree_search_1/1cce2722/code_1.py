import sys
from collections import Counter

# Read input from stdin
n = int(input())
sequence = list(map(int, input().split()))

# Count the occurrences of each number
freq_map = Counter(sequence)
max_ai = max(sequence)

# Initialize the dp array
dp = [0] * (max_ai + 1)

# Fill in the dp array
for i in range(1, max_ai + 1):
    take_i = freq_map[i] * i + (dp[i - 2] if i > 1 else 0)
    dont_take_i = dp[i - 1]
    dp[i] = max(take_i, dont_take_i)

# Output the answer
print(dp[max_ai])
