from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    stars = [[*map(int, line.split()), 0] for _ in range(n)]
    views = []
    
    # Process the initial brightness values
    for star in stars:
        x, y, s = star[:3]
        star[2] = min(s, 10)  # Adjusted the maximum brightness value to 10

    for _ in range(q):
        view_x1, view_y1, view_x2, view_y2 = map(int, input().split())
        views.append((view_x1, view_y1, view_x2, view_y2))

    dp = defaultdict(lambda: defaultdict(int))
    
    def update_dp(x, y):
        if x >= 0 and y >= 0:
            for star in stars:
                sx, sy, sc = star
                if sx <= x and sy <= y and sc > 0:
                    dp[x][y] += min(sc, 10)
                    
    for view_x1, view_y1, view_x2, view_y2 in views:
        update_dp(view_x1 - 1, view_y1 - 1)
        update_dp(view_x2, view_y2)
        
    # Now we have the maximum brightness values calculated
    for x in range(101):
        for y in range(101):
            print(dp[x][y])
