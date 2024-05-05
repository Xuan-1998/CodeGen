import sys
from collections import defaultdict

def min_operations(n, parents, ranges):
    # Build an adjacency list for the tree
    adj_list = defaultdict(list)
    for i in range(1, n):
        adj_list[parents[i]].append(i)

    # Initialize a dictionary to store the minimum and maximum values for each vertex
    min_max_vals = {i: (float('inf'), -float('inf')) for i in range(n)}

    def dfs(vertex):
        if min_max_vals[vertex][0] != float('inf') or min_max_vals[vertex][1] != -float('inf'):
            return

        min_val, max_val = float('inf'), -float('inf')
        for child in adj_list[vertex]:
            min_val, max_val = min(min_val, *min_max_vals[child]), max(max_val, *min_max_vals[child])
        min_max_vals[vertex] = (min_val, max_val)

    # Perform DFS to compute the minimum and maximum values for each vertex
    for i in range(1, n):
        dfs(i)

    # Calculate the minimum number of operations required to adjust each vertex
    ops = 0
    for i in range(n):
        min_val, max_val = min_max_vals[i]
        if ranges[i][0] > max_val or ranges[i][1] < min_val:
            ops += 1

    return ops

# Read input from stdin and write output to stdout
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    parents = [int(x) for x in sys.stdin.readline().split()]
    ranges = []
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().split())
        ranges.append((l, r))
    print(min_operations(n, parents, ranges))
