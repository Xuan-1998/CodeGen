def can_reach_last_index(jumps):
    curr_idx = 0
    max_jump = 0
    
    for i in range(len(jumps)):
        if i > curr_idx:
            return False
        
        max_jump = max(max_jump, jumps[i])
        
        curr_idx += max_jump + 1
    
    return True

# Example usage:
jumps = [2, 3, 1, 1, 4]
print(can_reach_last_index(jumps))  # Output: True
