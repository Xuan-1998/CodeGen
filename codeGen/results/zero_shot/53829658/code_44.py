import sys
from collections import defaultdict, deque

def tree_capital():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
    
    # Calculate the level of each node
    level = {i: 0 for i in range(1, n+1)}
    queue = deque([(1, 0)])  # Start from node 1 with level 0
    while queue:
        node, lev = queue.popleft()
        if lev > level[node]:
            level[node] = lev
            for neighbor in graph[node]:
                queue.append((neighbor, lev + 1))
    
    # Choose the capital city as the node with the smallest level
    capital = min(level, key=level.get)
    
    # Calculate the number of roads to be reversed from the capital
    rev_count = sum(1 for neighbor in graph if level[capital] > level[neighbor])
    
    return capital, rev_count

capital, rev_count = tree_capital()
print(rev_count)
print(' '.join(map(str, [i+1 for i in range(n) if i != capital])))
