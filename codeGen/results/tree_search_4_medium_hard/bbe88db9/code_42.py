import sys

n = int(sys.stdin.readline())
portals = [int(x) for x in sys.stdin.readline().split()]
result = min_portal_moves(n, portals)
print(result)
