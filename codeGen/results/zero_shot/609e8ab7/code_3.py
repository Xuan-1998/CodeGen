from collections import deque
T = int(input())  # number of test cases
for _ in range(T):
    n = int(input())  # number of vertices
    parent = list(map(int, input().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, input().split())
        ranges.append((l, r))
    
    # find the root node
    root = 1
    while parent[root-1] != -1:
        root = parent[root-1]
    
    # use a BFS to calculate the minimum number of operations for each node
    queue = deque([root])
    visited = set()
    min_ops = [0, *map(int, input().split())][:-1]
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        
        # calculate the minimum number of operations for this node
        l, r = ranges[node-1]
        if min_ops[node-2] > l and min_ops[node-2] < r:  # not on the edge
            ops = (l - min_ops[node-2]) + (r - min_ops[node-2])
        else:
            ops = 0
        
        queue.extend((i for i in range(node) if parent[i-1] == node and i not in visited))
    
    print(sum(ops for ops, _ in zip(min_ops[1:], ranges)))
