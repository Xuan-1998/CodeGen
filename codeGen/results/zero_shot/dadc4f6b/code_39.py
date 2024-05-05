# Read input
n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append(((t, x1, y1), (x2, y2)))

brightness = get_brightness(stars, views)
for b in brightness:
    print(b)
