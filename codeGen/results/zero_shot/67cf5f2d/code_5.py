def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    # Sort points by their positions
    points.sort()
    
    # Determine the optimal position for the new point
    max_position = points[-1][0]
    new_point_position = max_position + 1
    
    # Simulate activation from right to left
    furthest_removed = float('inf')
    removed_count = 0
    
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        if ai + bi < furthest_removed:
            removed_count += 1
            furthest_removed = ai
    
    # Print the number of points removed
    print(removed_count)

if __name__ == "__main__":
    main()

