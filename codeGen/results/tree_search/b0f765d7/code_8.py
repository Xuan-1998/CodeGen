import sys

def bitmask_from_vitamins(vitamins):
    mask = 0
    if 'A' in vitamins:
        mask |= 1 << 2
    if 'B' in vitamins:
        mask |= 1 << 1
    if 'C' in vitamins:
        mask |= 1
    return mask

# Read input
n = int(input())
juices = [(int(price), set(vitamins)) for price, vitamins in (input().split() for _ in range(n))]

# Initialize dp array
dp = [0] + [float('inf')] * 7

# Update dp array
for price, vitamins in juices:
    juice_mask = bitmask_from_vitamins(vitamins)
    for mask in range(8):
        new_mask = mask | juice_mask
        dp[new_mask] = min(dp[new_mask], dp[mask] + price)

# Output the result
print(dp[7] if dp[7] < float('inf') else -1)
