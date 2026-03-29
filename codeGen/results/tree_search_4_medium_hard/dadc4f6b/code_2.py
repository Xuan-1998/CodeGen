def solve():
    n, q, c = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))
    
    dp = [[0] * (c + 1) for _ in range(q + 1)]
    
    def f(t, r):
        if t > q:
            return 0
        total_brightness = 0
        for x1, y1, x2, y2 in r:
            if all(x1 <= x <= x2 and y1 <= y <= y2 for x, y, s in stars):
                total_brightness += sum(s for _, _, s in stars)
        dp[t][c] = total_brightness
        return total_brightness
    
    for t in range(q, 0, -1):
        r = []
        for _ in range(n):
            x1, y1, x2, y2 = map(int, input().split())
            if all(x1 <= x <= x2 and y1 <= y <= y2 for x, y, s in stars):
                r.append((x1, y1, x2, y2))
        total_brightness = f(t, r)
    
    print(dp[q][c])

if __name__ == "__main__":
    solve()
