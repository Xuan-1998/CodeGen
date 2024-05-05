code
import sys

def read_input():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

n, m, edges = read_input()
