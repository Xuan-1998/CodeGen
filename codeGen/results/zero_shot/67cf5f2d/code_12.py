python
def minimize_removed_points(n, points):
    # Sort points based on their positions in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize the number of points removed to 0
    removed_points = 0
    # The farthest point to the left that has been removed
    farthest_removed = -1
    
    # Iterate through the points from right to left
    for pos, rng in points:
        if pos + rng > farthest_removed:
            # This point will be activated and remove points to its left
            removed_points += 1
            # Update the farthest removed point
            farthest_removed = pos
    
    # Return the number of points removed
    return removed_points

if __name__ == "__main__":
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
    
    result = minimize_removed_points(n, points)
    print(result)

