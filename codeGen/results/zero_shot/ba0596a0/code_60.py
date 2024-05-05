def can_cross_stones(stone_positions):
    # Initialize previous jump distance
    prev_jump = 0
    
    for i in range(1, len(stone_positions)):
        # Calculate current jump distance
        curr_jump = abs(stone_positions[i] - stone_positions[i-1])
        
        # Check if the frog can jump from this stone to the next one
        if curr_jump not in [prev_jump - 1, prev_jump, prev_jump + 1]:
            return False
        
        # Update previous jump distance
        prev_jump = curr_jump
    
    # If we reached the last stone without jumping into the water, return True
    return True

# Read input from standard input
stone_positions = [int(x) for x in input().split()]

# Print answer to standard output
print(can_cross_stones(stone_positions))
