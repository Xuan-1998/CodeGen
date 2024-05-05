import sys

# Read input
n, q = map(int, sys.stdin.readline().split())
stars = [[0] * 2 for _ in range(n)]
for i in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars[i][0], stars[i][1] = x, y
    stars[i].append(s)

# Sort the stars by their initial brightness in descending order
stars.sort(key=lambda x: x[2], reverse=True)

# Create a 3D table of size (100+1)*(100+1)*10
brightness = [[[0 for _ in range(11)] for _ in range(101)] for _ in range(101)]

for i, star in enumerate(stars):
    for j in range(max(0, star[0]-9), min(100, star[0]+10)):
        for k in range(max(0, star[1]-9), min(100, star[1]+10)):
            brightness[j][k][min(10, 10-star[2])] += 1

# Read queries
for _ in range(q):
    x1, y1, t = map(int, sys.stdin.readline().split())
    x2, y2 = min(100, max(0, x1+9)), min(100, max(0, y1+9))
    ans = sum(brightness[x][y][t] for x in range(x1, x2+1) for y in range(y1, y2+1))
    print(ans)
