import heapq
from collections import defaultdict

n, q, c = map(int, input().split())
stars = []
memo = {}

for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

def total_brightness(x1, y1, x2, y2):
    if (x1, y1) in memo:
        return memo[(x1, y1)]
    pq = []
    for star in stars:
        x, y, s = star
        if x1 <= x <= x2 and y1 <= y <= y2:
            heapq.heappush(pq, -s)
    total_brightness = 0
    while pq:
        total_brightness += -heapq.heappop(pq)
    memo[(x1, y1)] = total_brightness
    return total_brightness

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(total_brightness(x1, y1, x2, y2))
