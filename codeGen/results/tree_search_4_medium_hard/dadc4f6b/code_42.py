import sys
from collections import defaultdict

def total_brightness():
    n, q, c = map(int, input().split())
    
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))
    
    dp = defaultdict(int)
    for t in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        
        # Add 1 to the time for each step of time passed since the last update
        t += 1
        
        total_brightness = 0
        for star in stars:
            x, y, s = star
            
            # Check if a star is not visible due to its y-coordinate being outside the view's top and bottom boundaries or its x-coordinate being outside the view's left and right boundaries
            if (y1 <= y <= y2) and (x1 <= x <= x2):
                total_brightness += s
        
        dp[(x1, y1, x2, y2)] = min(c, total_brightness + t)
    
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[(x1, y1, x2, y2)])

total_brightness()
