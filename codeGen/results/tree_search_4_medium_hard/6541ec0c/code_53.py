import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

values = [int(x) for x in sys.stdin.readline().split()]
edges = [(int(u), int(v)) for u, v in (line.split() for line in sys.stdin.readlines()[2:])]

print(solve(n, k, values, edges))
