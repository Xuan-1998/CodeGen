from collections import defaultdict

def total_brightness(n, c, stars, q, views):
    # Initialize memoized table with default value as 0
    dp = [[[0] * (c + 1) for _ in range(101)] for _ in range(101)]

    def update_brightness(state, t):
        x1, y1, x2, y2 = state
        total_brightness = 0
        for star in stars:
            if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:
                # Update brightness based on time
                brightness = min(c, int((t - star[2]) * (c / 10)))
                total_brightness += brightness
        return total_brightness

    for view in views:
        x1, y1, x2, y2, t = view
        if dp[y1][x1][t] == 0:  # Memoization check
            dp[y1][x1][t] = update_brightness((x1, y1, x2, y2), t)
        print(dp[y1][x1][t])

if __name__ == "__main__":
    n, q, c = map(int, input().split())
    stars = [list(map(int, input().split())) for _ in range(n)]
    views = [list(map(int, input().split())) for _ in range(q)]
    total_brightness(n, c, stars, q, views)
