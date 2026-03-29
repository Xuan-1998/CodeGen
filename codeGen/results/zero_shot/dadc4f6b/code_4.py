import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, (x1, y1), (x2, y2)))

for view in views:
    t, ((x1, y1), (x2, y2)) = view
    total_brightness = 0
    for star in stars:
        x, y, s = star
        if x1 <= x <= x2 and y1 <= y <= y2:  # check if the star is within the view
            total_brightness += min(c, s)  # add the minimum of c and s to the total brightness
    print(total_brightness)
