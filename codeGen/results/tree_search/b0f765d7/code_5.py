import sys

# Function to convert the vitamin string to a bitmask
def vitamins_to_mask(vitamins):
    mask = 0
    for vitamin in vitamins:
        if vitamin == 'A':
            mask |= 1  # Set the first bit
        elif vitamin == 'B':
            mask |= 2  # Set the second bit
        elif vitamin == 'C':
            mask |= 4  # Set the third bit
    return mask

# Read the number of juices
n = int(input().strip())

# Initialize the dp array
dp = [float('inf')] * 8
dp[0] = 0  # Base case: no vitamins cost 0

# Process each juice
for _ in range(n):
    cost, vitamins = input().strip().split()
    cost = int(cost)
    mask = vitamins_to_mask(vitamins)

    # Update the dp table
    for prev_mask in range(8):
        new_mask = prev_mask | mask
        dp[new_mask] = min(dp[new_mask], dp[prev_mask] + cost)

# The answer is the minimum cost to obtain all three vitamins
answer = dp[7] if dp[7] != float('inf') else -1
print(answer)
