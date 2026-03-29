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

dp = [[0] * 101 for _ in range(10001)]
for i in range(n):
    x, y, s = stars[i]
    t_max = min(x, c) - 1
    for j in range(t_max + 1):
        if j <= x:
            dp[j][y] += s

ans = []
for view in views:
    t, (x1, y1), (x2, y2) = view
    total_brightness = 0
    for i in range(y1 - 1, y2 + 1):
        if x1 <= x2 and dp[t][i] > c:
            total_brightness += c
        else:
            total_brightness += min(dp[t][i], c)
    ans.append(total_brightness)

for answer in ans:
    print(answer)
