python
def minimize_removals(n, points):
    # Sort points based on their coordinates
    points.sort()
    
    # Active points set
    active_points = set()
    
    # To hold the number of removals for each point
    removals = [0] * n
    
    # Iterate from right to left
    for i in range(n-1, -1, -1):
        ai, bi = points[i]
        # Remove points within the range of the current point
        removal_count = 0
        for j in range(i-1, -1, -1):
            if points[j][0] >= ai - bi:
                removal_count += 1
            else:
                break
        removals[i] = removal_count
    
    # The additional point to the right won't remove any points
    # We need to find the minimum removals among the existing points
    min_removals = min(removals)
    
    return min_removals

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
    
    result = minimize_removals(n, points)
    print(result)

