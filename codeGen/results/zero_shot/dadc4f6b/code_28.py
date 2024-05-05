codeblock
import sys

# Initialize variables
n, q, c = map(int, sys.stdin.readline().split())
stars = {}
views = []

# Read star information
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars[(x, y)] = s

# Read view information
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append((t, (x1, y1), (x2, y2)))

# Calculate total brightness for each view
results = []
for view in views:
    t, ((x1, y1), (x2, y2)) = view
    brightness = 0
    for star in stars:
        if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:
            brightness += min(c, stars[star])
    results.append(brightness)

# Print the results
for result in results:
    print(result)
