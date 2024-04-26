import sys

def find_min_durability(n, coordinates, durabilities):
    # Add the durability of infinity for bearing points
    durabilities = [float('inf')] + durabilities + [float('inf')]
    
    # Calculate the initial segment lengths
    segment_lengths = [coordinates[i+1] - coordinates[i] for i in range(n+1)]
    
    # Simulate the collapse process
    while True:
        collapse = False
        for i in range(1, n+1):
            # If the segment length exceeds the durability, collapse occurs
            if segment_lengths[i] > durabilities[i]:
                # Redistribute the load to neighboring points
                segment_lengths[i-1] += segment_lengths[i] / 2
                segment_lengths[i+1] += segment_lengths[i] / 2
                segment_lengths[i] = 0
                collapse = True
                break
        # If no collapse occurred, we are done
        if not collapse:
            break
    
    # Find the maximum segment length after collapses
    max_segment_length = max(segment_lengths)
    
    # The minimum durability required is the max segment length
    return max_segment_length

# Read input from stdin
n = int(input().strip())
coordinates = list(map(int, input().strip().split()))
durabilities = list(map(int, input().strip().split()))

# Calculate and print the result
min_durability = find_min_durability(n, coordinates, durabilities)
# If the minimum durability is infinite, we do not need to add a point
print(0 if min_durability == float('inf') else int(min_durability))

