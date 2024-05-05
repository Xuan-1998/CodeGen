def can_reach_last_index(jumps):
    current_position = 0
    max_jump = jumps[0]
    
    for i in range(1, len(jumps)):
        if i > current_position:
            return False
        
        if i == len(jumps) - 1:
            return True
        
        max_jump = min(max_jump, jumps[i])
        current_position += max_jump + 1
    
    return True

# Test the function
jumps = [2,3,1,1,4]
print(can_reach_last_index(jumps))  # Output: True
