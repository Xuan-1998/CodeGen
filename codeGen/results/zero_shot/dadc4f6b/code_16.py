import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append(((t, (x1, y1), (x2, y2)), 0))  # Initialize total brightness for each view

def get_brightness(star, view):
    x1, y1 = view[1]
    x2, y2 = view[2]
    if star[0] >= x1 and star[0] <= x2 and star[1] >= y1 and star[1] <= y2:
        return min(c, star[2])
    else:
        return 0

total_brightness = []
for view in views:
    t, _, _ = view[0]
    brightness = 0
    for star in stars:
        brightness += get_brightness(star, view)
    total_brightness.append(brightness)

for brightness in total_brightness:
    print(brightness)
