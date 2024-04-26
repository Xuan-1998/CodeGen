from collections import Counter
import sys

def read_integers():
    return list(map(int, sys.stdin.readline().strip().split()))

n = int(input())
sequence = read_integers()

# Step 1: Count the frequency of each number in the sequence
frequency = Counter(sequence)

# Step 2: Set up the dp array
max_element = max(sequence)
dp = [0] * (max_element + 1)

# Step 3: Fill the dp array
for i in range(1, max_element + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + i * frequency[i] if i in frequency else 0)

# Step 4: Output the answer
print(dp[max_element])
