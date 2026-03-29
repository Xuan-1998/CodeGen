from collections import deque

def min_operations(n, parent, ranges):
    memo = {}
    visited = set()
    queue = [(0, 0)]  # (node, adjustment)

    while queue:
        node, adj = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == 1:  # root node
                res = 0
            else:
                parent_node = parent[node]
                res = memo.get(parent_node, float('inf')) - (ranges[node][1] - ranges[parent_node][1])
            for child in range(2, n+1):
                if child == node:
                    continue
                if child not in visited:
                    queue.append((child, adj))
                    memo[child] = res + 1

    return min(memo.values())

n = int(input())
parent = [0] + list(map(int, input().split()))
ranges = []
for _ in range(n):
    l, r = map(int, input().split())
    ranges.append((l, r))

print(min_operations(n, parent, ranges))
