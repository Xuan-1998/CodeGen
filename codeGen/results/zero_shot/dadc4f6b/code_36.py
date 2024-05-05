import sys

def total_brightness(star, view):
    x1, y1, x2, y2 = view
    if (x1 <= star[0] <= x2) and (y1 <= star[1] <= y2):
        return star[2]
    else:
        return 0

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))
views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, x1, y1, x2, y2))

result = []
for view in views:
    total_brightness_in_view = sum(total_brightness(star, view) for star in stars)
    result.append(str(total_brightness_in_view))

print('\n'.join(result))
