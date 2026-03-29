import sys

n, q = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

dp_table = [[0] * (q + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    x, y, s = stars[i - 1]
    dp_table[i][0] += s

for j in range(1, q + 1):
    t, x1, y1, x2, y2 = map(int, input().split())
    for i in range(n + 1):
        if (i == n or stars[i - 1][0] > x2 or stars[i - 1][1] < y1):
            break
        while stars[i - 1][0] >= x1 and stars[i - 1][0] <= x2:
            dp_table[i][j] += min(stars[i - 1][2], c)
            i -= 1

for j in range(q + 1):
    print(dp_table[0][j])
