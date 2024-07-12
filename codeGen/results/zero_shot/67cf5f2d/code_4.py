python
def minimize_removed_points(n, points):
    # Sort points based on position in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    removed_points = set()
    min_removed = n  # Start with the worst case where all points are removed
    
    for i in range(n):
        ai, bi = points[i]
        current_removed = 0
        # Simulate activation of points from right to left
        for j in range(i, n):
            aj, bj = points[j]
            if aj not in removed_points:
                current_removed += 1
                # Mark points within range to the left as removed
                for k in range(j + 1, n):
                    ak, bk = points[k]
                    if ak >= aj - bj:
                        removed_points.add(ak)
                    else:
                        break
        # Update the minimum removed points
        min_removed = min(min_removed, current_removed)
        removed_points.clear()
    
    return min_removed

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
    
    result = minimize_removed_points(n, points)
    print(result)

