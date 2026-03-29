import sys

def can_cross_stones(stone_positions):
    max_jump = 0
    for i in range(1, len(stone_positions)):
        if abs(stone_positions[i] - stone_positions[i-1]) > max_jump + 2:
            return False
        max_jump = max(max_jump, abs(stone_positions[i] - stone_positions[i-1]))
    return True

# Read input from stdin
stone_positions = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(can_cross_stones(stone_positions))
