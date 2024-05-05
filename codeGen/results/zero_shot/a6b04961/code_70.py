import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, edges

def find_max_beauty(n, edges):
    # Sort the edges by their length
    sorted_edges = sorted(edges, key=lambda x: abs(x[0] - x[1]))

    # Initialize variables for maximum beauty and current tail
    max_beauty = 0
    current_tail = [edges[0][0]]

    for edge in sorted_edges:
        if edge[0] == current_tail[-1]:
            current_tail.append(edge[1])
        else:
            if len(current_tail) > 1:
                max_beauty = max(max_beauty, (len(current_tail) - 1) * (edge[0] - current_tail[-2]))
            current_tail = [edge[0]]

    # Calculate the beauty of the last tail
    max_beauty = max(max_beauty, len(current_tail) + 1)

    return max_beauty

n, edges = read_input()
max_beauty = find_max_beauty(n, edges)
print(max_beauty)
