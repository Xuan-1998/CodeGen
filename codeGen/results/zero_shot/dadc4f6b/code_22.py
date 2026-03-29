n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append({'x': x, 'y': y, 's': s})
views = []
for _ in range(q):
    t, ll_x, ll_y, ur_x, ur_y = map(int, input().split())
    views.append({'t': t, 'll_x': ll_x, 'll_y': ll_y, 'ur_x': ur_x, 'ur_y': ur_y})

def calc_brightness(view):
    brightness = 0
    for star in stars:
        if (star['x'] >= view['ll_x'] and star['x'] <= view['ur_x'] and
                star['y'] >= view['ll_y'] and star['y'] <= view['ur_y']):
            brightness += min(star['s'], c)
    return brightness

for view in views:
    t = view['t']
    ll_x, ll_y, ur_x, ur_y = view['ll_x'], view['ll_y'], view['ur_x'], view['ur_y']
    # Calculate the total brightness for this view
    brightness = calc_brightness(view)
    print(brightness)
