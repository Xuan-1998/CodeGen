from collections import Counter
import sys

# Read input from stdin
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Count the occurrences of each number in the sequence
count = Counter(a)

# Initialize the dp array
max_value = max(a)
dp = [0] * (max_value + 1)

# Update the dp array according to the intuition provided
for i in range(1, max_value + 1):
    if i > 1:
        dp[i] = max(dp[i-1], dp[i-2] + i * count[i])
    else:
        dp[i] = i * count[i]

# The last element of the dp array contains the maximum points that can be earned
print(dp[max_value])
