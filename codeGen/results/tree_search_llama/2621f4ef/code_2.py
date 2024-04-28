import sys

def calculate_area(mines):
    # Find the convex hull of the mines
    from shapely.geometry import Polygon
    points = [(x, y) for x, y in mines]
    hull = Polygon(points).convex_hull
    
    # Calculate the area as the product of the lengths of the two chords
    a = hull.length
    b = (hull.area ** 0.5)
    return a * b

def main():
    n = int(sys.stdin.readline().strip())
    mines = []
    
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        mines.append((x, y))
    
    area = calculate_area(mines)
    print(area)

if __name__ == "__main__":
    main()
