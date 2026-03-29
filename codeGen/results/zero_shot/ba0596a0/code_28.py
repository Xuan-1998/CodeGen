import sys

stones = [int(x) for x in sys.stdin.read().split()]
print(frog_can_cross(stones))
