def minimize_removed_points(n, points):
    # Sort points based on their positions
    points.sort()
    
    # Initialize variables
    max_range = float('-inf')
    removed_points = 0
    result = n  # Start with the worst case where all points are removed
    
    # Traverse points from right to left
    for i in range(n - 1, -1, -1):
        position, range_ = points[i]
        max_range = max(max_range, position + range_)
        # Calculate number of points that will be removed
        removed_points = n - i - 1  # points to the right of current point
        result = min(result, removed_points)
    
    return result

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
    
    print(minimize_removed_points(n, points))

