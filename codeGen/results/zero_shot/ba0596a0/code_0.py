import sys

def can_cross_stones(stone_positions):
    # Check if the first stone is at position 0 (required)
    if stone_positions[0] != 0:
        return False
    
    for i in range(1, len(stone_positions)):
        # Calculate the difference between consecutive stone positions
        diff = stone_positions[i] - stone_positions[i-1]
        
        # Check if the jump constraint is satisfied
        if not (diff == 1 or diff == 2 or diff == 3):
            return False
    
    return True

# Read input from stdin
stone_positions = list(map(int, sys.stdin.readline().split()))

# Print the result to stdout
print(can_cross_stones(stone_positions))
