python
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
    points.sort(reverse=True)
    
    # To keep track of the number of points removed
    removed_count = 0
    max_position = -1
    
    for ai, bi in points:
        if ai + bi > max_position:
            removed_count += 1
            max_position = ai
    
    print(removed_count)

# Call the function
minimize_removed_points()

