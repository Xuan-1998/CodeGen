def can_frog_cross(stones):
    can_cross = True
    for i in range(1, len(stones)):
        if abs(stones[i] - stones[i-1]) not in [k-1 for k in range(2, min(i+3, len(stones))+1)]:
            can_cross = False
            break
    return can_cross

# Read input from stdin
stones = list(map(int, input().split()))

# Print the answer to stdout
print(can_frog_cross(stones))
