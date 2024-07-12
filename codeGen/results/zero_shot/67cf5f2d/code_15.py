def minimize_removed_points(n, points):
    # Sort points by position in descending order (right to left)
    points.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize variables
    removed_count = 0
    rightmost_position = points[0][0] + 1  # Place the additional point at max(ai) + 1
    
    # Track the farthest left point that has been removed
    farthest_left_removed = float('inf')
    
    # Process each point from right to left
    for ai, bi in points:
        if ai + bi >= farthest_left_removed:
            # This point would have already been removed
            removed_count += 1
        else:
            # Update the farthest left point that will be removed
            farthest_left_removed = ai - bi
    
    return removed_count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    result = minimize_removed_points(n, points)
    print(result)

