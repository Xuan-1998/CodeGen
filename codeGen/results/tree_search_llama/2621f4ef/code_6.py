import sys

mine_coords = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    mine_coords.append((x, y))

print(min_area_mines(mine_coords))
