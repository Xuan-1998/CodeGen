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

total_brightnesses = []
for view in views:
    total_brightness = 0
    for star in stars:
        if min(star[:2]) >= view[1][0] and max(star[:2]) <= view[2][0] and \
           min(star[:2]) >= view[1][1] and max(star[:2]) <= view[2][1]:
            total_brightness += min(c, star[2])
    total_brightnesses.append(total_brightness)

for brightness in total_brightnesses:
    print(brightness)
