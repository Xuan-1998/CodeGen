import sys

def read_inputs():
    n = int(sys.stdin.readline())
    mines = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        mines.append((x, y))
    return mines

def find_min_area(mines):
    # Sort the mines by x-coordinate
    mines.sort(key=lambda p: p[0])

    min_x, max_x = mines[0][0], mines[0][0]
    for x, _ in mines:
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x

    # Sort the mines by y-coordinate
    mines.sort(key=lambda p: p[1])

    min_y, max_y = mines[0][1], mines[0][1]
    for _, y in mines:
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y

    # Calculate the minimum area of the city
    return (max_x - min_x) * (max_y - min_y)

def main():
    mines = read_inputs()
    min_area = find_min_area(mines)
    print(min_area)

if __name__ == "__main__":
    main()
