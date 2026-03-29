import sys

def calculate_brightness(stars, x_ll, y_ll, x_ur, y_ur):
    # Calculate total brightness in this view
    brightness = 0
    for star in stars:
        if (x_ll <= star[0] <= x_ur) and (y_ll <= star[1] <= y_ur):
            brightness += star[2]
    return brightness

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, min(s, c)))

views = []
for _ in range(q):
    t, x_ll, y_ll, x_ur, y_ur = map(int, sys.stdin.readline().split())
    views.append(((t, x_ll, y_ll), (x_ur, y_ur)))

for view in views:
    time, x_ll, y_ll = view[0]
    x_ur, y_ur = view[1]
    brightness = calculate_brightness(stars, x_ll, y_ll, x_ur, y_ur)
    print(brightness)
