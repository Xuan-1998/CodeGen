def total_brightness(n, q, c):
    memo = {}
    def calc_brightness(s_i, x1, y1, x2, y2, t):
        if (s_i, x1, y1, t) not in memo:
            if t < min(x for x, s_x in enumerate(s_i)):
                return 0
            brightness = sum(s_i[x] * (1 - abs(x-x1)/c) for x in range(min(x1,x2), max(x1,x2)+1) if s_x > 0)
            memo[(s_i, x1, y1, t)] = brightness
        return memo[(s_i, x1, y1, t)]

    stars = [list(map(int, input().split())) for _ in range(n)]
    views = [tuple(map(int, input().split())) for _ in range(q)]
    
    total_brightness_values = []
    for view in views:
        t, x1, y1, x2, y2 = view
        brightness = 0
        for star in stars:
            s_i, x, y = star
            if min(x1,x2) <= x <= max(x1,x2) and min(y1,y2) <= y <= max(y1,y2):
                brightness += calc_brightness(s_i, x1, y1, x2, y2, t)
        total_brightness_values.append(brightness)

    print(*total_brightness_values, sep='\n')
