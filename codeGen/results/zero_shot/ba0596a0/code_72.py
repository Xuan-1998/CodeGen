def can_cross_stones(stones):
    can_cross = True
    for i in range(1, len(stones)):
        if stones[i] - stones[i-1] not in [k - 1 for k in range(max(1, stones[i-1]))]:
            can_cross = False
            break
    return can_cross

# Read input from stdin
stones = list(map(int, input().split()))

# Print the answer to stdout
print(can_cross_stones(stones))
