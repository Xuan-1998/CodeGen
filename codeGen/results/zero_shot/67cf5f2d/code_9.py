def minimize_removed_points():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(n)]
    
    # Sort the points by their position ai
    points.sort()
    
    # Initialize an array to keep track of the minimum points removed
    removed = [0] * n
    
    # Iterate from right to left
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Determine the farthest left point that can be removed by point i
        j = i - 1
        while j >= 0 and points[j][0] >= ai - bi:
            j -= 1
        # If j is -1, it means no point to the left can be removed
        if j == -1:
            removed[i] = 1
        else:
            removed[i] = removed[j] + 1
    
    # We need to add one point to the right of all existing points
    min_removed = min(removed)
    
    # Output the minimum number of points that could be removed
    print(min_removed)

# Call the function to execute
minimize_removed_points()

