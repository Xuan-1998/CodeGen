from collections import defaultdict

n, q, c = map(int, input().split())
stars = defaultdict(dict)
for _ in range(n):
    x, y, s = map(int, input().split())
    stars[x][y] = s

dp = [[0] * 101 for _ in range(101)]

for i in range(100 + 1):
    for j in range(100 + 1):
        for k, v in stars.items():
            if k <= i and j <= v:
                dp[i][j] += v[k][v]

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

result = []
for t, ((x1, y1), (x2, y2)) in views:
    total_brightness = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if dp[i][j] > c:
                total_brightness += c
            else:
                total_brightness += dp[i][j]
    result.append(total_brightness)

print(*result, sep='\n')
