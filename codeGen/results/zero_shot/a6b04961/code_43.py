import sys

def find_max_beauty(n, m, edges):
    # Initialize variables
    max_beauty = 0
    tails = []
    for _ in range(n):
        tails.append([])

    # Find all possible tails
    for edge in edges:
        u, v = edge
        if not tails[u-1]:
            tails[u-1] = [v]
        else:
            for i, vertex in enumerate(tails[u-1]):
                if vertex == v:
                    break
            tails[u-1].pop(i)
        tails[v-1].append(u)

    # Calculate beauty for each tail
    for tail in tails:
        if not tail:
            continue
        beauty = len(tail) * (m - len(tail))
        max_beauty = max(max_beauty, beauty)

    return max_beauty

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Calculate and print the maximum possible beauty
max_beauty = find_max_beauty(n, m, edges)
print(max_beauty)
