import sys

def can_cross_stones(stone_positions):
    # Check if the input list has at least 2 stones
    if len(stone_positions) < 2:
        raise ValueError("The input list must have at least 2 stones")

    # Initialize a variable to store the distance of the previous jump
    prev_jump_distance = stone_positions[1] - stone_positions[0]

    for i in range(1, len(stone_positions) - 1):
        # Calculate the distance between the current stone and the next one
        curr_jump_distance = stone_positions[i + 1] - stone_positions[i]

        # Check if the distance is either one less than, equal to, or one more than the previous jump
        if not (curr_jump_distance == prev_jump_distance - 1 or
                curr_jump_distance == prev_jump_distance or
                curr_jump_distance == prev_jump_distance + 1):
            return False

        # Update the previous jump distance for the next iteration
        prev_jump_distance = curr_jump_distance

    return True

# Read input from stdin
stone_positions = [int(x) for x in sys.stdin.readline().split()]

# Print the output to stdout
print(can_cross_stones(stone_positions))
