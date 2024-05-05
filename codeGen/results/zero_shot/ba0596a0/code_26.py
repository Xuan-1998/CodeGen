def can_cross_river(stones):
    prev_position = 0
    for position in stones:
        # Check if the frog can jump to this stone
        if abs(position - prev_position) not in [1, 2]:
            return False
        prev_position = position
    return True

# Read input from stdin
stones = [int(x) for x in input().split()]

# Print output to stdout
print(can_cross_river(stones))
