n = int(input())
dp = [0] + [float('inf')] * 7

for _ in range(n):
    cost, vitamins = input().split()
    cost = int(cost)
    mask = 0
    if 'A' in vitamins:
        mask |= 1  # Set the rightmost bit
    if 'B' in vitamins:
        mask |= 2  # Set the middle bit
    if 'C' in vitamins:
        mask |= 4  # Set the leftmost bit
    
    # Update dp values for all combinations with the current juice
    for i in range(8):
        dp[i | mask] = min(dp[i | mask], dp[i] + cost)

# Output the answer
print(dp[7] if dp[7] != float('inf') else -1)
