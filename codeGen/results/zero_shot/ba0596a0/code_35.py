def can_cross_river(stones):
    # Initialize variables
    last_stone = len(stones) - 1
    prev_jump = 0
    
    for i in range(len(stones) - 1):
        jump = stones[i + 1] - stones[i]
        
        if jump != (prev_jump + 1) and jump != (prev_jump + 2) and jump != (prev_jump + 3):
            return False
        
        prev_jump = jump
    
    # Check if the frog can reach the last stone
    if stones[last_stone] - stones[-2] not in [0, 1, 2]:
        return False
    
    return True

# Receive input from stdin and print answer to stdout
stones = list(map(int, input().split()))
print(can_cross_river(stones))
