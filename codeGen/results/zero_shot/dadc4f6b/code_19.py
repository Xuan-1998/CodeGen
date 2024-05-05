def solve():
    n, q, c = map(int, input().split())
    stars = []
    
    # Read star information
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))
    
    # Sort stars by x-coordinate
    stars.sort(key=lambda star: star[0])
    
    views = []
    
    # Read view information
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        
        # Calculate the total brightness of stars in this view
        total_brightness = 0
        
        for star in stars:
            if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:  # Check if the star is within the view
                total_brightness += min(c, star[2])  # Add the maximum brightness of this star to the total
        
        views.append(total_brightness)
    
    for brightness in views:
        print(brightness)

if __name__ == "__main__":
    solve()
