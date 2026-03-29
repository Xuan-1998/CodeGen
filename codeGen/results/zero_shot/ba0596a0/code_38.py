def can_cross_stones(stones):
    n = len(stones)
    
    # The frog starts on the first stone
    current_position = 0
    
    for i in range(n - 1):
        jump_distance = stones[i + 1] - stones[i]
        
        if jump_distance < 2 or (jump_distance % 3) != 0:
            return False
        
        # Update the frog's position
        current_position += jump_distance
    
    return True

# Example usage:
stones = [0, 3, 5, 7, 10, 12]
print(can_cross_stones(stones))  # Output: True
