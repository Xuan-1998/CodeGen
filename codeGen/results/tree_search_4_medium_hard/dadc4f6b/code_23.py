# Read input
n, q = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

# Initialize memoized table
memo = {(0, 0): 0}

def calculate_brightness(state):
    i, j = state
    return sum(s for x, y, s in stars if x >= views[views.index((t, (x1, y1), (x2, y2)))[1][0] and y >= views[views.index((t, (x1, y1), (x2, y2)))[1][1] and x <= views[views.index((t, (x1, y1), (x2, y2)))[2][0] and y <= views[views.index((t, (x1, y1), (x2, y2)))[2][1]] and j < c) for s in stars[i:i+j])

# Process queries
for t, (x1, y1), (x2, y2) in views:
    i = 0
    j = 0
    for x, y, s in stars:
        if x >= x1 and y >= y1 and x <= x2 and y <= y2:
            i += 1
            j = max(j, s)
    print(memo.get((i, j), calculate_brightness((i, j))))
