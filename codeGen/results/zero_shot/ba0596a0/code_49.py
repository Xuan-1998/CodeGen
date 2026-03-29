import sys

stones = [int(x) for x in sys.stdin.readline().split()]
last_stone = stones[-1]

curr_pos = 0
max_jump = 2

for stone in stones:
    while curr_pos < stone - 1 and max_jump > 1:
        curr_pos += max_jump
        if max_jump == k:
            max_jump += 1
        else:
            max_jump -= 1
    if curr_pos >= stone:
        break
    else:
        curr_pos = stone - 1

if curr_pos >= last_stone:
    print(True)
else:
    print(False)
