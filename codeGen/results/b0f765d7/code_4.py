import sys

# Read the number of juices from stdin
n = int(input())

# Initialize the dp array with infinity for all states except the empty set
dp = [0 if mask == 0 else float('inf') for mask in range(8)]

# A helper function to convert a string of vitamins to a bitmask
def vitamins_to_mask(vitamins):
    mask = 0
    if 'A' in vitamins:
        mask |= 1  # Set the first bit
    if 'B' in vitamins:
        mask |= 2  # Set the second bit
    if 'C' in vitamins:
        mask |= 4  # Set the third bit
    return mask

# Process each juice and update the dp table
for _ in range(n):
    cost, vitamins = input().split()
    cost = int(cost)
    mask = vitamins_to_mask(vitamins)
    
    # Update the dp table
    for prev_mask in range(8):
        new_mask = prev_mask | mask
        dp[new_mask] = min(dp[new_mask], dp[prev_mask] + cost)

# The final answer is the minimum cost to obtain all vitamins (mask 111 in binary, which is 7)
answer = dp[7]

# If the answer is still infinity, it means it's impossible to obtain all vitamins
if answer == float('inf'):
    print(-1)
else:
    print(answer)
