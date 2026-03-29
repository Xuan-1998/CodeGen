import sys

def dfs(vertex, parent_range):
    # Initialize the minimum number of operations
    min_ops = 0
    
    # Calculate the range for this vertex
    vertex_range = (parent_range[1] - parent_range[0]) // 2 + parent_range[0]
    
    # If the vertex is within its range, no ops are needed
    if l[vertex] <= vertex_range <= r[vertex]:
        return min_ops
    
    # Otherwise, calculate the number of operations
    diff = abs(vertex_range - l[vertex])
    if diff > 0:
        min_ops += diff // (vertex_range - parent_range[0]) + 1
    diff = abs(r[vertex] - vertex_range)
    if diff > 0:
        min_ops += diff // (r[vertex] - vertex_range) + 1
    
    return min_ops

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
l = []
r = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    l.append(line[0])
    r.append(line[1])

# Initialize the minimum number of operations
min_ops = 0

# Perform DFS from each vertex to its root
for i in range(2, n+1):
    parent_range = (l[p[i]], r[p[i]])
    min_ops += dfs(i, parent_range)

print(min_ops)
