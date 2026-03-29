import sys
from collections import defaultdict

def solve():
    # Read input
    n, m, T = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        graph[u].append((v, t))

    # TO DO: implement the rest of the solution

if __name__ == "__main__":
    solve()
