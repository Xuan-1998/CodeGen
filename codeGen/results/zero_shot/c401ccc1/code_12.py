import sys

def infinite_zoo_graph():
    q = int(sys.stdin.readline())
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        if (u & v) == v:
            print("YES" if has_path(u, v) else "NO")

def has_path(u, v):
    visited = set()
    stack = [(u, [u])]
    while stack:
        node, path = stack.pop(0)
        if node == v:
            return True
        for next_node in range(2**30):  # iterate over all vertices
            if (node & next_node) == next_node and next_node not in visited:
                stack.append((next_node, path + [next_node]))
                visited.add(next_node)
    return False

infinite_zoo_graph()
