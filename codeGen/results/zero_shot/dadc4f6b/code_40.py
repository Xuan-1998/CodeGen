import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))

for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    total_brightness = 0
    for star in stars:
        if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:
            total_brightness += min(star[2], c)
    print(total_brightness)
