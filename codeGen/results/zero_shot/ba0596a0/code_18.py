import sys

def can_frog_cross(stones):
    # Calculate the maximum distance the frog can cover in each jump
    max_jump_distance = (stones[-1] - stones[0]) // (3 + 1)

    # Check if the frog can always find a stone to jump from within the allowed distances
    for i, (prev_stone, current_stone) in enumerate(zip(stones[:-1], stones[1:])):
        distance = current_stone - prev_stone
        if distance > max_jump_distance:
            return False

    return True

# Read input from stdin
stones = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(can_frog_cross(stones))
