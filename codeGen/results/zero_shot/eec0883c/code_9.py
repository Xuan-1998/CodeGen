import sys

# Read input from stdin
n = int(sys.stdin.readline().strip())
w = list(map(int, sys.stdin.readsplitlines()[1:]))
graph = []
for _ in range(n-1):
    u, v, c = map(int, sys.stdin.readline().strip().split())
    graph.append((u, v, c))

# TO DO: implement the solution
