import sys

def can_frog_cross(stones):
    # Find the minimum jump distance (k)
    min_jump = (stones[1] - stones[0]) // 3
    
    for i in range(2, len(stones)):
        # Calculate the expected position after jumping from the previous stone
        expected_position = stones[i-1] + min_jump
        
        # Check if the expected position matches the current stone's position
        if expected_position != stones[i]:
            return False  # Frog cannot cross
    
    return True  # Frog can cross

# Read input from stdin
stones = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(can_frog_cross(stones))
