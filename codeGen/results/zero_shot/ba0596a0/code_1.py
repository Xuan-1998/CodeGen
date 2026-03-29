import sys

def can_frog_cross(stones):
    can_cross = True
    k = 0
    for i in range(1, len(stones)):
        jump_dist = stones[i] - stones[i-1]
        if abs(jump_dist - k) > 2:
            can_cross = False
            break
        k = jump_dist
    print(can_cross)

# Read input from stdin and pass it to the function
input_stones = list(map(int, sys.stdin.readline().split()))
can_frog_cross(input_stones)
