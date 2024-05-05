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

brightnesses = []
for view in views:
    total_brightness = 0
    for star in stars:
        if star[0] >= view[1][0] and star[0] < view[2][0] and star[1] >= view[1][1] and star[1] < view[2][1]:
            total_brightness += star[2]
    brightnesses.append(total_brightness)

for b in brightnesses:
    print(b)
