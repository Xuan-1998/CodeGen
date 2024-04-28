import sys

def read_input():
    n = int(sys.stdin.readline())
    mines = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        mines.append((x, y))
    return mines

def find_min_enclosing_rectangle(mines):
    min_x = max_x = min_y = max_y = None
    for x, y in mines:
        if min_x is None or x < min_x:
            min_x = x
        if max_x is None or x > max_x:
            max_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_y is None or y > max_y:
            max_y = y

    width = max_x - min_x
    height = max_y - min_y
    return (min_x, min_y), (width, height)

def calculate_area(min_enclosing_rectangle):
    (x, y), (w, h) = min_enclosing_rectangle
    return w * h

if __name__ == "__main__":
    mines = read_input()
    min_enclosing_rectangle = find_min_enclosing_rectangle(mines)
    area = calculate_area(min_enclosing_rectangle)
    print(area)
