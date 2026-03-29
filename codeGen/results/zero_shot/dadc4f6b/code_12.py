def total_brightness():
    n, q, c = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    views = []
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        views.append((t, (x1, y1), (x2, y2)))

    brightnesses = [0] * q

    for star_x, star_y, s in stars:
        for i, (view_t, view_ll, view_ur) in enumerate(views):
            if min(view_ll) <= star_x <= max(view_ur) and min(view_ll[1]) <= star_y <= max(view_ur[1]):
                brightnesses[i] += int(s * (view_t / 10**9))

    for i, b in enumerate(brightnesses):
        print(min(c, b))
