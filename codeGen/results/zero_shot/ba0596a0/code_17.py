import sys

def can_frog_cross(stones):
    mid = len(stones) // 2
    last_stone = stones[-1]
    distance_to_last_stone = last_stone - stones[mid]

    if distance_to_last_stone in [i for i in range(-1, 3)]:
        return True
    else:
        return False

# Read input from stdin
stones = [int(x) for x in sys.stdin.readline().split()]

# Call the function and print the result
print(can_frog_cross(stones))
