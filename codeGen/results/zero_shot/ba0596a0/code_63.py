import sys

def can_cross_stones(stones):
    # Step 1: Initialize the minimum jump distance
    min_jump = 0
    
    for i in range(1, len(stones)):
        # Step 2: Calculate the difference between consecutive stones
        diff = stones[i] - stones[i-1]
        
        if diff != min_jump + 1 and diff != min_jump:
            return False
        
        min_jump += 1
    
    return True

# Read input from stdin
stones = list(map(int, sys.stdin.readline().split()))

# Call the function to check if the frog can cross
result = can_cross_stones(stones)

# Print the result to stdout
print(result)
