import sys

stones = []
for line in sys.stdin:
    stones.append(int(line.strip()))

last_position = 0
can_cross = True

for stone in stones[1:]:  # start from the second stone
    jump_distance = stone - last_position
    if abs(jump_distance) not in [k-1, k, k+1] for k in range(1, int(abs(jump_distance)) + 1):
        can_cross = False
        break
    last_position = stone

print(can_cross)
