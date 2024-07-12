python
def minimize_removed_points():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        ai = int(data[index])
        bi = int(data[index + 1])
        points.append((ai, bi))
        index += 2
    
    # Sort points based on their positions
    points.sort()
    
    # Initialize the rightmost position for the additional point
    rightmost_position = points[-1][0] + points[-1][1] + 1
    
    # Track the number of points that would be removed
    removed_count = 0
    min_removed = n
    
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        if ai + bi >= rightmost_position:
            removed_count += 1
        else:
            rightmost_position = ai
            min_removed = min(min_removed, removed_count)
    
    # Output the minimum number of points removed
    print(min_removed)

# Call the function to execute
minimize_removed_points()

