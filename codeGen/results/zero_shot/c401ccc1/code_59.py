def dfs(u, v):
    visited = set()
    stack = [(u, [u])]

    while stack:
        node, path = stack.pop()
        if node == v:
            return "YES"
        if node in visited:
            continue
        visited.add(node)
        for next_node in range(node + 1, 2**30):
            if node & next_node == next_node:
                stack.append((next_node, path + [next_node]))
    return "NO"

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if dfs(u, v) else "NO")
