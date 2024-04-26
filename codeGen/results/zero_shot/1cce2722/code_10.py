from collections import Counter
import sys

# Step 1: Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Step 2: Calculate frequency of each element
frequency = Counter(a)

# Step 3: Initialize DP array
max_value = max(a)
dp = [0] * (max_value + 1)

# Step 4: Compute DP values
for i in range(1, max_value + 1):
    dp[i] = max(dp[i-1], dp[i-2] + i * frequency[i])

# Step 5: The answer is the last element in the DP array
answer = dp[max_value]

# Step 6: Output the answer
print(answer)
