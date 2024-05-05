import sys

n = int(sys.stdin.readline())
q = int(sys.stdin.readline())
c = int(sys.stdin.readline())

stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))

stars.sort(key=lambda x: (x[0], x[1]))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, (x1, y1), (x2, y2)))

for t, (x1, y1), (x2, y2) in views:
    total_brightness = 0
    for star in stars:
        if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:
            total_brightness += star[2]
    print(total_brightness)
