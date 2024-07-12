python
def main():
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
    
    # We will use a list to keep track of the points that are still active
    active_points = []
    removed_count = 0
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        
        # Remove points that are within the range of the current point
        while active_points and active_points[-1] >= ai - bi:
            active_points.pop()
            removed_count += 1
        
        # Add current point to the list of active points
        active_points.append(ai)
    
    # The new point will be added to the right of all existing points
    # It will not remove any additional points since it is to the right of all
    # existing points.
    
    # Output the number of points removed
    print(removed_count)

if __name__ == "__main__":
    main()

