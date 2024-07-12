python
def minimize_removals(n, points):
    # Sort points based on their coordinates
    points.sort()
    
    # Initialize a list to keep track of active points
    active_points = []
    min_removed = n  # Start with the worst case where all points are removed

    # Traverse from right to left
    for i in range(n-1, -1, -1):
        ai, bi = points[i]
        # Remove points that are within bi distance to the left of ai
        while active_points and active_points[-1] >= ai - bi:
            active_points.pop()
        
        # Add the current point to the active points list
        active_points.append(ai)
        
        # Calculate the number of points removed if we add the new point after this point
        min_removed = min(min_removed, len(active_points))
    
    return min_removed

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
points = []
for i in range(n):
    ai = int(data[2*i + 1])
    bi = int(data[2*i + 2])
    points.append((ai, bi))

# Calculate the result
result = minimize_removals(n, points)

# Print the result
print(result)

