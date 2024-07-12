python
def max_points(n, sequence):
    # Step 1: Create a frequency array
    max_val = 105
    freq = [0] * (max_val + 1)
    for num in sequence:
        freq[num] += 1

    # Step 2: Define the dp array
    dp = [0] * (max_val + 1)

    # Step 3: Initialize base cases
    dp[0] = 0
    dp[1] = freq[1]

    # Step 4: Fill the dp array using the transition relation
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + freq[i] * i)

    # Step 5: The result is in dp[max_val]
    return dp[max_val]

# Reading input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Get the result and print it
result = max_points(n, sequence)
print(result)

