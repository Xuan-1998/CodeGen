python
import sys
input = sys.stdin.read

def min_removed_points(n, points):
    # Sort points based on the coordinates ai
    points.sort()

    # Array to keep track of points that would be removed
    removed = [0] * n

    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        # If the current point is within the range of the next point
        if points[i][0] + points[i][1] >= points[i + 1][0]:
            removed[i] = removed[i + 1] + 1
        else:
            removed[i] = removed[i + 1]
    
    # The minimum number of points removed if we add a point at the end
    return removed[0]

def main():
    data = input().split()
    n = int(data[0])
    points = []
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))

    result = min_removed_points(n, points)
    print(result)

if __name__ == "__main__":
    main()

