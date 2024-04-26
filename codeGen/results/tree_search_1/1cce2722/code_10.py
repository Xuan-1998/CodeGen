from collections import Counter
import sys

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

# Count the frequency of each element in the sequence
freq = Counter(a)

# Initialize the dp list
max_value = max(a)
dp = [0] * (max_value + 1)

# Calculate the maximum points for each value
for i in range(1, max_value + 1):
    if i == 1:
        # Base case: only one value to consider
        dp[i] = freq[i] * i
    else:
        # Choose the best between not taking i or taking i and adding its score
        dp[i] = max(dp[i-1], dp[i-2] + freq[i] * i)

# The last element of dp will hold the maximum points that can be achieved
print(dp[max_value])
