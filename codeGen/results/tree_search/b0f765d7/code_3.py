n = int(input())
dp = [0 if mask == 0 else float('inf') for mask in range(8)]

for _ in range(n):
    price, vitamins = input().split()
    price = int(price)
    juice_bitmask = 0
    if 'A' in vitamins:
        juice_bitmask |= 1
    if 'B' in vitamins:
        juice_bitmask |= 2
    if 'C' in vitamins:
        juice_bitmask |= 4
    
    # Update dp for the new mask
    for mask in range(8):
        new_mask = mask | juice_bitmask
        dp[new_mask] = min(dp[new_mask], dp[mask] + price)

# We want all vitamins, so we check dp[7] which corresponds to bitmask 111
if dp[7] == float('inf'):
    print(-1)
else:
    print(dp[7])
