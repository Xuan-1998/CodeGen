import sys
from bisect import bisect_left

n, q = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

c = int(input())

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (min(x1, x2), min(y1, y2)), max(x1, x2), max(y1, y2)))

# Sort stars by x-coordinate
stars.sort()

memo = {}
def get_brightness(t, r):
    if (t, tuple(sorted([x1i, x2i] + [y1i, y2i])) for x1i, y1i, x2i, y2i in views[:q]) in memo:
        return memo[(t, tuple(sorted([x1i, x2i] + [y1i, y2i]) for x1i, y1i, x2i, y2i in views[:q]))]
    
    total_brightness = 0
    rectangles = []
    current_x1 = None
    current_y1 = None
    for star in stars:
        x, y, s = star
        if (x > r[1] or y > r[3]):
            continue
        if (x < r[0] or y < r[2]):
            if current_x1 is not None and current_y1 is not None:
                rectangles.append((r[0], r[2], sum(s for x, y, s in stars if x >= r[0] and x <= r[2] and y >= r[1] and y <= r[3]))))
            r = (x, y)
        elif (current_x1 is None or current_y1 is not None):
            current_x1 = x
            current_y1 = y

    rectangles.sort(key=lambda r: r[0])
    total_brightness += sum(s for x, y, s in stars if x >= r[2] and y <= r[3])
    
    memo[(t, tuple(sorted([x1i, x2i] + [y1i, y2i]) for x1i, y1i, x2i, y2i in views[:q]))] = total_brightness
    return total_brightness

total_brightness = 0
for view in views:
    t, r = view
    total_brightness += get_brightness(t, r)

print(total_brightness)
