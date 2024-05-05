import sys

n, q = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

memo = {}

def query(x1, y1, x2, y2, t):
    key = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2), t)
    if key in memo:
        return memo[key]
    
    total_brightness = 0
    for star in stars:
        x, y, s = star
        if (x >= x1 and x <= x2) or (y >= y1 and y <= y2):
            if t <= star[2]:  # only consider stars that are still on
                total_brightness += s
    
    memo[key] = total_brightness
    return total_brightness

for _ in range(q):
    x1, y1, x2, y2, t = map(int, input().split())
    print(query(x1, y1, x2, y2, t))
