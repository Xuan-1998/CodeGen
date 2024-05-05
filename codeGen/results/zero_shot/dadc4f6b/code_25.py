import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = []
views = []

for _ in range(n):
    x, y, si = map(int, sys.stdin.readline().split())
    stars.append((x, y, si))

for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, (x1, y1), (x2, y2)))

