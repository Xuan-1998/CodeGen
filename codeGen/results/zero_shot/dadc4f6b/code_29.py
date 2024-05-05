n = int(input())
q = int(input())
stars = []
for i in range(n):
    x, y, si = map(int, input().split())
    stars.append((x, y, si))

views = []
for i in range(q):
    t, xl, xu, yl, yu = map(int, input().split())
    views.append((t, (xl, xu), (yl, yu)))

for view in views:
    t, (xl, xu), (yl, yu) = view
    total_brightness = 0
    for star in stars:
        x, y, si = star
        if xl <= x <= xu and yl <= y <= yu:
            total_brightness += si
    print(total_brightness)
