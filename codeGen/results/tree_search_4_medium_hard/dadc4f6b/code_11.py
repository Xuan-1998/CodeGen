import sys

n, q = map(int, input().split())
c = int(input())

stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

table = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(11)]

for t in range(11):
    for x in range(101):
        for y in range(101):
            if t > 0:
                table[t][x][y] = table[t-1][x][y]
                for star in stars:
                    if star[0] <= x and star[1] <= y:
                        table[t][x][y] += star[2]

for view in views:
    t, (x1, y1), (x2, y2) = view
    print(sum(table[min(t, 10)][min(x, 100)][min(y, 100)] for x in range(max(x1, 0), min(x2+1, 101)) 
           for y in range(max(y1, 0), min(y2+1, 101))))
