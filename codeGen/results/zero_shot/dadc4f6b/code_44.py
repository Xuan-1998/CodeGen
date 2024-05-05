import sys
from collections import defaultdict

def solve():
    n, q, c = map(int, input().split())
    
    # Store star coordinates and initial brightness in a dictionary
    stars = {}
    for _ in range(n):
        x, y, s = map(int, input().split())
        if (x, y) not in stars:
            stars[(x, y)] = s
        else:
            stars[(x, y)] += s
    
    # Process each query
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        
        # Initialize total brightness to 0
        total_brightness = 0
        
        # Iterate over the stars within the view rectangle
        for (x, y) in [(i, j) for i in range(x1, x2+1) for j in range(y1, y2+1)]:
            if (x, y) in stars:
                total_brightness += stars[(x, y)]
        
        # Print the total brightness
        print(total_brightness)

if __name__ == "__main__":
    solve()
