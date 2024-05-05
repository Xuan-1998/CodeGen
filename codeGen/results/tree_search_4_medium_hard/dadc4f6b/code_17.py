from collections import defaultdict

n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append(((x1, y1), (x2, y2)))

# Memoization table
memo = defaultdict(dict)

def calculate_brightness(star, view):
    (x1, y1), (x2, y2) = view
    t, x, y, s = star[3], star[0], star[1], star[2]
    
    if (s, x, y, t) in memo:
        return memo[(s, x, y, t)]
    
    # Calculate the state of this star at time t
    brightness = 0
    if s <= c and x1 <= x <= x2 and y1 <= y <= y2:
        brightness = s
    
    memo[(s, x, y, t)] = brightness
    return brightness

ans = []
for view in views:
    total_brightness = 0
    for star in stars:
        if (star[0] >= view[0][0] and star[0] <= view[1][0] and 
            star[1] >= view[0][1] and star[1] <= view[1][1]):
            total_brightness += calculate_brightness(star, view)
    ans.append(total_brightness)

print('\n'.join(map(str, ans)))
