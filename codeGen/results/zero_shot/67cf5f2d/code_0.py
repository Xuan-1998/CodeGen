def minimize_removed_points(n, points):
    # Sort points by their positions in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize variables
    removed_points = 0
    active_points = set()
    
    # Iterate through the points from right to left
    for ai, bi in points:
        # Remove points within the range [ai - bi, ai]
        to_remove = set()
        for point in active_points:
            if ai - bi <= point <= ai:
                to_remove.add(point)
        
        # Update the set of active points
        active_points -= to_remove
        removed_points += len(to_remove)
        
        # Add the current point to the set of active points
        active_points.add(ai)
    
    # The number of points removed is minimized by adding the new point
    return removed_points

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]
    
    result = minimize_removed_points(n, points)
    print(result)

