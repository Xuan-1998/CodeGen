def can_frog_cross(stones):
    k = stones[1] - stones[0]
    
    for i in range(2, len(stones)):
        if abs(stones[i] - stones[i-1]) != k and abs(stones[i] - stones[i-1]) != k+1:
            return False
    
    return True
