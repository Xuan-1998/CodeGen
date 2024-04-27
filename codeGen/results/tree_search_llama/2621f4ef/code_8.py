import sys

def min_city_area(mines):
    mines.sort()
    n = len(mines)

    def find_min_area(x_coords, y_coords):
        # Find the maximum x-coordinate for each group of y-coordinates
        max_x_coords = [max(x) for x in zip(*x_coords)]
        max_y_coords = [max(y) for y in zip(*y_coords)]

        # Calculate the area for each group
        areas = [(max_x - min_x) * (max_y - min_y) for ((min_x, _), (max_x, _)), ((_ , min_y), ( _, max_y)) in zip(x_coords, y_coords)]
        return sum(areas)

    if n <= 1:
        return 0

    mid = mines[n // 2]
    above_mines = [(x, y) for x, y in mines if y < mid]
    below_mines = [(x, y) for x, y in mines if y >= mid]

    # Recursively find the minimum area for each group
    area_above = find_min_area(*zip(*above_mines))
    area_below = find_min_area(*zip(*below_mines))

    return area_above + area_below

# Read input from stdin
n = int(sys.stdin.readline())
mines = [list(map(int, line.split())) for _ in range(n)]

# Print the minimum possible area to stdout
print(min_city_area(mines))
