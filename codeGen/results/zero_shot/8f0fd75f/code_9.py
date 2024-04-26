def find_min_durability(n, coordinates, durabilities):
    # Calculate the initial segments lengths
    segments = [coordinates[i+1] - coordinates[i] for i in range(n+1)]
    
    # Simulate the collapse process
    while True:
        collapse = False
        for i in range(1, n+1):
            # Check if the current segment exceeds the durability of the point
            if segments[i] > durabilities[i-1]:
                # Redistribute the load to the neighboring points
                segments[i-1] += segments[i] - durabilities[i-1]
                segments[i] = durabilities[i-1]
                collapse = True
                break
        if not collapse:
            break
    
    # Find the critical point and calculate the minimum durability required
    max_segment = max(segments[1:-1])
    min_durability = max_segment if max_segment > max(durabilities) else 0
    
    return min_durability

# Read input from stdin
n = int(input().strip())
coordinates = list(map(int, input().strip().split()))
durabilities = list(map(int, input().strip().split()))

# Calculate and print the result
print(find_min_durability(n, coordinates, durabilities))
