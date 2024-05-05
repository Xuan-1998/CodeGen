def can_cross_stones(stone_positions):
    # Initialize the distance of the previous jump
    prev_jump_distance = 0
    
    for stone_position in stone_positions:
        # Calculate the maximum possible jump from the current position
        max_possible_jump = prev_jump_distance + 2
        
        if stone_position > prev_jump_distance + max_possible_jump:
            return False
        
        prev_jump_distance = abs(stone_position - prev_jump_distance)
        
    return True

stone_positions = [int(x) for x in input().split()]
print(can_cross_stones(stone_positions))
