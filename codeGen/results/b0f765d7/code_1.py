# Read the number of juices
n = int(input())

# Initialize the dp array with infinity for all combinations except the empty set
dp = [float('inf')] * 8
dp[0] = 0

# Function to convert vitamin string to bitmask
def vitamins_to_mask(vitamins):
    mask = 0
    if 'A' in vitamins:
        mask |= 1 << 0
    if 'B' in vitamins:
        mask |= 1 << 1
    if 'C' in vitamins:
        mask |= 1 << 2
    return mask

# Iterate over each juice
for _ in range(n):
    cost, vitamins = input().split()
    cost = int(cost)
    juice_mask = vitamins_to_mask(vitamins)
    
    # Update the dp array with the new juice
    for old_mask in range(8):
        new_mask = old_mask | juice_mask
        dp[new_mask] = min(dp[new_mask], dp[old_mask] + cost)

# The answer is the minimum cost to obtain all vitamins (mask 0b111)
answer = dp[7] if dp[7] != float('inf') else -1
print(answer)
