import sys

def calculate_brightness(n, q, c):
    stars = []
    views = []

    # Read in stars and views from standard input
    for _ in range(n):
        x, y, s = map(int, sys.stdin.readline().split())
        stars.append((x, y, s))

    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        views.append((t, (x1, y1), (x2, y2)))

    # Iterate over each view and calculate the total brightness
    for view in views:
        t, ((x1, y1), (x2, y2)) = view
        total_brightness = 0

        for star in stars:
            x, y, s = star
            if x1 <= x <= x2 and y1 <= y <= y2:
                total_brightness += s

        print(total_brightness)

if __name__ == "__main__":
    n, q, c = map(int, sys.stdin.readline().split())
    calculate_brightness(n, q, c)
