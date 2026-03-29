import sys

n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

dp = [[0] * (101) for _ in range(11010)]
for i, ((x1, y1), (x2, y2)) in enumerate(stars):
    for t in range(max(x1, y1, x2, y2) + 1):
        if t >= x1 and t <= x2 and t >= y1 and t <= y2:
            dp[t][i] = min(c, stars[i][2])

for i, (t, ((x1, y1), (x2, y2))) in enumerate(views):
    max_brightness = 0
    for j in range(max(x1, y1, x2, y2) + 1):
        if all(x <= j and j <= y for x, y in [(x1, y1), (x2, y2)]):
            max_brightness = max(max_brightness, dp[j][i])
    print(max_brightness)
