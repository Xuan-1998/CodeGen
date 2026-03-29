import sys

n, q, c = map(int, input().split())
stars = [0] * n
for i in range(n):
    x, y, si = map(int, input().split())
    stars[i] = si

views = []
for _ in range(q):
    t_i, x1, y1, x2, y2 = map(int, input().split())
    views.append((t_i, (x1, y1), (x2, y2)))

brightness = []
for view in views:
    t_i, ((x1, y1), (x2, y2)) = view
    total_brightness = 0
    for star in stars:
        x, y = star[0], star[1]
        if x1 <= x <= x2 and y1 <= y <= y2:
            # Calculate the current brightness of this star
            current_brightness = min(c, si * (t_i - t_i // c))
            total_brightness += current_brightness
    brightness.append(total_brightness)

for i, b in enumerate(brightness):
    print(b)
