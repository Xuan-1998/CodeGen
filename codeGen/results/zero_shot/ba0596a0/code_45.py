def can_cross_stones(stones):
    prev_jump = 0  # initial jump distance
    for stone in stones:
        if abs(stone - prev_jump) not in [1, 2, 3]:
            return False  # invalid jump, frog can't reach this stone
        prev_jump = stone  # update previous jump distance
    return True  # frog reached the last stone

# Read input from stdin
stones = list(map(int, input().split()))

# Print the answer to stdout
print(can_cross_stones(stones))
