def minimize_removed_points():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    # Sort points by position in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    # Track the number of points that can be removed
    active_points = set()
    removed_count = 0
    
    for ai, bi in points:
        # Remove points within range [ai - bi, ai]
        to_remove = {p for p in active_points if p >= ai - bi}
        removed_count += len(to_remove)
        active_points -= to_remove
        active_points.add(ai)
    
    # Add a new point to the right of all existing points
    new_point_position = max(p[0] for p in points) + 1
    
    # The new point won't remove any additional points
    print(removed_count)

minimize_removed_points()

