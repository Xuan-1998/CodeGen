def f(t, x1, x2, y1, y2):
    if t == 0:
        return sum(s_i for i in range(n) if min(x2, x_i) <= x_i <= max(x2, x_i) and min(y2, y_i) <= y_i <= max(y2, y_i))
    
    total_brightness = 0
    for i in range(n):
        if min(x2, x_i) <= x_i <= max(x2, x_i) and min(y2, y_i) <= y_i <= max(y2, y_i):
            total_brightness += s_i
    
    memo[t][x1][x2][y1][y2] = total_brightness
    return total_brightness

n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, brightness = map(int, input().split())
    stars.append((x, y, brightness))

memo = {}

total_brightnesses = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    total_brightnesses.append(f(t, x1, x2, y1, y2))
    
print('\n'.join(map(str, total_brightnesses)))
