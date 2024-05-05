import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = {}
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars[(x, y)] = s

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, (x1, y1), (x2, y2)))

def calculate_brightness(view):
    t, (x1, y1), (x2, y2) = view
    total_brightness = 0
    for star in stars:
        x, y = star
        if x1 <= x <= x2 and y1 <= y <= y2:
            total_brightness += s
    return total_brightness

brightnesses = []
for view in views:
    brightnesses.append(calculate_brightness(view))

print("\n".join(map(str, brightnesses)))
