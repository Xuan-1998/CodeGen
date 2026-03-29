import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s_i = map(int, sys.stdin.readline().split())
    stars.append((x, y, s_i))

views = []
for _ in range(q):
    t_i, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t_i, (x1, y1), (x2, y2)))

brightnesses = []
for view in views:
    t_i, (x1, y1), (x2, y2) = view
    visible_stars = 0
    for star in stars:
        x, y, s_i = star
        if x1 <= x <= x2 and y1 <= y <= y2:  # Check visibility
            visible_stars += s_i
    brightnesses.append(visible_stars)

for brightness in brightnesses:
    print(brightness)
