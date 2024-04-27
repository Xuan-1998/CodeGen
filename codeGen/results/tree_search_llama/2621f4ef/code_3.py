import sys
import math

n = int(sys.stdin.readline())
mines = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    mines.append((x, y))

max_x = max(x for x, y in mines)
max_y = max(y for x, y in mines)

side_length = max(max_x, max_y)
area = side_length ** 2
print(area)
