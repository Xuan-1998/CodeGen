def can_cross_river(stones):
    if len(stones) < 2:
        return False
    
    min_jump = stones[1] - stones[0]
    
    for i in range(1, len(stones)-1):
        current_jump = stones[i+1] - stones[i]
        if abs(current_jump - min_jump) > 1 or (current_jump < min_jump and current_jump != 1):
            return False
        min_jump = current_jump
    
    return True

# Read input from stdin
stones = list(map(int, input().split()))

# Call the function and print the result to stdout
print(can_cross_river(stones))
