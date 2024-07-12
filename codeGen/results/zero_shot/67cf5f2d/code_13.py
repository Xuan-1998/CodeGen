python
def minimize_removed_points(n, points):
    # Sort points by their positions in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    removed_count = 0
    max_position = points[0][0] + 1  # Position of the new point to the right of all existing points
    active_points = []

    for pos, range_ in points:
        # Remove points from active_points that are no longer in range
        while active_points and active_points[-1] < pos - range_:
            active_points.pop()
        
        # Activate current point
        active_points.append(pos)
        
        # If the new point is added, it would have removed this point
        if max_position - pos <= range_:
            removed_count += 1
    
    return removed_count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]
    
    result = minimize_removed_points(n, points)
    print(result)

