python
def minimize_removed_points(n, points):
    # Sort points by their position
    points.sort()
    
    # Initialize the count of removed points
    removed_count = 0
    
    # Initialize the earliest position that can be removed
    earliest_removal = float('inf')
    
    # Iterate from right to left
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        
        # Check if this point is within the range of removal
        if ai < earliest_removal:
            # This point is not removed, update the earliest removal position
            earliest_removal = ai - bi
        else:
            # This point is removed
            removed_count += 1
    
    return removed_count

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
points = []

for i in range(n):
    ai = int(data[2 * i + 1])
    bi = int(data[2 * i + 2])
    points.append((ai, bi))

# Add an additional point to the right of all existing points
additional_point = (max(points, key=lambda x: x[0])[0] + 1, 0)
points.append(additional_point)

# Calculate the minimum number of points removed
result = minimize_removed_points(n + 1, points)
print(result)

