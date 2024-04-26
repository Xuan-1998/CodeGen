from collections import Counter

# Read the number of elements in the sequence
n = int(input())

# Read the sequence of integers
sequence = list(map(int, input().split()))

# Count the frequency of each element in the sequence
count = Counter(sequence)

# Initialize the dp array with zeros
# We need to handle the case where the maximum element is greater than n
max_value = max(sequence)
dp = [0] * (max_value + 1)

# Base cases
dp[0] = 0
dp[1] = count[1]

# Populate the dp array using the given intuition
for i in range(2, max_value + 1):
    dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)

# The answer is the maximum points that can be earned considering all elements
print(dp[max_value])
