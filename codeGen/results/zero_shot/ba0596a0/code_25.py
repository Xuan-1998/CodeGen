def can_cross_stones():
    # Read input from standard input
    stones = list(map(int, input().split()))
    
    # Initialize last stone position as -1
    last_stone_position = -1
    
    # Iterate through each stone position
    for i in range(len(stones)):
        # Calculate the minimum and maximum possible jump distance
        min_jump_distance = abs(last_stone_position - stones[i]) // 2
        max_jump_distance = abs(last_stone_position - stones[i])
        
        # Check if the frog can reach the current stone from the previous one
        for j in range(min_jump_distance, max_jump_distance + 1):
            if (last_stone_position + j) == stones[i]:
                last_stone_position = stones[i]
                break
        
        # If the frog cannot reach the current stone, return False
        else:
            return False
    
    # If the frog can reach all stones, return True
    return True

# Read input from standard input and print the output to standard output
print(can_cross_stones())
