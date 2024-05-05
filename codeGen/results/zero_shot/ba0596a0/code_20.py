python
def can_cross_stones(stones):
    # Initialize the current position at 0 (the first stone)
    current_position = 0
    
    # Iterate through the stones
    for target_position in stones:
        # Calculate the maximum jump distance based on the current position and the previous jump
        max_jump_distance = abs(target_position - current_position) // 2 * 2
        
        # If we can't reach the target stone, return False
        if abs(target_position - current_position) > max_jump_distance + 1:
            return False
        
        # Update the current position for the next iteration
        current_position = target_position
    
    # If we've reached all stones without jumping into the water, return True
    return True

# Read the input from standard input
stones = [int(x) for x in input().split()]

# Print the result to standard output
print(can_cross_stones(stones))
