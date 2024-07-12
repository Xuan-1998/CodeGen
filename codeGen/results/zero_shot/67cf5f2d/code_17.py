python
def minimize_removed_points(n, points):
    # Sort points by their coordinate in descending order
    points.sort(reverse=True, key=lambda x: x[0])

    # Initialize variables
    removed_points = 0
    furthest_left_removed = float('inf')

    # Simulate activation from right to left
    for ai, bi in points:
        if ai + bi < furthest_left_removed:
            furthest_left_removed = ai
        else:
            removed_points += 1

    return removed_points

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

