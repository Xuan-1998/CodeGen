# Define a function can_cross_river to check if the frog can cross the river
def can_cross_river(stones):
    # Initialize the current position of the frog as 0 (the first stone)
    current_position = 0
    
    # Iterate over each stone in the list
    for i in range(1, len(stones)):
        # Calculate the distance to the next stone
        distance_to_next_stone = stones[i] - stones[i-1]
        
        # Check if the frog can jump to the next stone
        if distance_to_next_stone < 3: 
            current_position += distance_to_next_stone
        else:
            return False
    
    # If the frog has reached the last stone, return True
    return True

# Read input from standard input
stones = list(map(int, input().split()))

# Print the result to standard output
print(can_cross_river(stones))
