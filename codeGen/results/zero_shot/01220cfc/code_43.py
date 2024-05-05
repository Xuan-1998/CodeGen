def can_reach_last_index(jumps):
    last_idx = len(jumps) - 1
    current_idx = 0
    
    while current_idx <= last_idx:
        if current_idx == last_idx:
            return True
        
        jumps_left = min(last_idx, current_idx + jumps[current_idx])
        
        for i in range(current_idx + 1, jumps_left + 1):
            if i == last_idx:
                return True
            current_idx = i
    
    return False

jumps = list(map(int, input().split()))
print(can_reach_last_index(jumps))
