code
n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s_i = map(int, input().split())
    stars.append((x, y, s_i))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append(((x1, y1), (x2, y2)))

brightnesses = []
for view in views:
    total_brightness = 0
    for star in stars:
        if min(star[:2]) <= view[0][0] and max(star[:2]) >= view[0][0] and min(star[:2]) <= view[0][1] and max(star[:2]) >= view[0][1]:
            total_brightness += star[2]
    brightnesses.append(total_brightness)

for brightness in brightnesses:
    print(brightness)
