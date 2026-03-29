import sys

def read_input():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

def find_max_beauty(n, m, edges):
    # Sort the edges by their endpoints
    edges.sort()

    max_beauty = 0
    tail_length = 0
    spines = set()
    for edge in edges:
        u, v = edge
        if u > v:  # Swap the order of the vertices if necessary
            u, v = v, u
        if v not in spines and (u + 1) % tail_length == 0:
            tail_length += 1
            spines.add(v)
        else:
            max_beauty = max(max_beauty, tail_length * len(spines))
    return max_beauty

n, m, edges = read_input()
print(find_max_beauty(n, m, edges))
