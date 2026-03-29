def can_cross_stones():
    stones = [int(x) for x in input().split()]
    
    if len(stones) < 2:
        return False
    
    last_jump_distance = stones[1] - stones[0]
    
    for i in range(1, len(stones)-1):
        current_jump_distance = stones[i+1] - stones[i]
        
        if abs(current_jump_distance - last_jump_distance) not in [1, 2]:
            return False
        
        last_jump_distance = current_jump_distance
    
    return True
