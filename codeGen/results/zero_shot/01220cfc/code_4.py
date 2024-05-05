def can_reach_last_index(jumps):
    last_idx = len(jumps) - 1
    curr_idx = 0
    
    while curr_idx <= last_idx:
        max_jump = jumps[curr_idx]
        next_idx = min(last_idx, curr_idx + max_jump)
        
        if next_idx >= last_idx:
            return True
        
        curr_idx = next_idx + 1
    
    return False

# Example usage
jumps = [2, 3, 1, 1, 4]
print(can_reach_last_index(jumps))  # Output: True
