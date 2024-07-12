def minimize_removals(n, points):
    # Sort points by position in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize variables
    removed = 0
    rightmost_removed = -1
    
    # Traverse points from right to left
    for a, b in points:
        if a + b > rightmost_removed:
            removed += 1
            rightmost_removed = a
    
    return removed

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    points = []
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    result = minimize_removals(n, points)
    print(result)

