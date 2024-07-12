python
def minimize_removed_points(n, points):
    # Sort points by position in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize the count of removed points
    removed_count = 0
    max_position = -1  # The farthest left position that has been removed
    
    # Simulate the activation process from right to left
    for ai, bi in points:
        if ai > max_position:
            removed_count += 1
            max_position = ai - bi - 1
    
    return removed_count

# Reading input from stdin
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
points = []
for i in range(n):
    ai = int(data[2 * i + 1])
    bi = int(data[2 * i + 2])
    points.append((ai, bi))

# Calculate the minimum number of points that could be removed
result = minimize_removed_points(n, points)

# Output the result
print(result)

