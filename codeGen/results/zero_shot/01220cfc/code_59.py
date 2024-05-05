def is_possible_to_reach_last_index(jump_array):
    n = len(jump_array)
    
    # Initialize the current position as 0
    current_position = 0
    
    for i in range(n - 1):
        # If we can't reach the next index, return False
        if i + jump_array[i] < i + 1:
            return False
        
        # Update the current position to the maximum reachable position
        current_position = i + jump_array[i]
    
    # If we can reach the last index, return True
    return True

# Read input from stdin
jump_array = [int(x) for x in input().split()]

# Print the result to stdout
print(is_possible_to_reach_last_index(jump_array))
