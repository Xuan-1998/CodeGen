from collections import defaultdict

def dp(t, x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return 0
    
    total_brightness = 0
    for i in range(n):  # iterate over stars
        if (x1 <= stars[i][0] <= x2) and (y1 <= stars[i][1] <= y2):
            total_brightness += stars[i][2]
    
    memo[(t, x1, y1, x2, y2)] = total_brightness
    
    return total_brightness

n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s_i = map(int, input().split())
    stars.append((x, y, min(s_i, c)))
    
memo = defaultdict(int)

for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    print(dp(t-1, x1-1, y1-1, x2-1, y2-1))
