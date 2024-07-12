python
def minimize_removals(n, points):
    # Sort points by position in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize variables
    removed_count = 0
    max_position = points[0][0]
    
    # Iterate over points
    for ai, bi in points:
        if ai + bi < max_position:
            removed_count += 1
        else:
            max_position = ai
    
    return removed_count

# Reading input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
points = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]

# Output the result
print(minimize_removals(n, points))

