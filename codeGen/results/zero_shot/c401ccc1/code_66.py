from sys import stdin

def dfs(u, v):
    visited = set()
    stack = [u]

    while stack:
        node = stack.pop()
        if node == v:
            return True
        if node not in visited:
            visited.add(node)
            next_node = node & v
            if next_node != node and next_node not in visited:
                stack.append(next_node)

    return False

q = int(stdin.readline())

for _ in range(q):
    u, v = map(int, stdin.readline().split())
    if dfs(u, v):
        print("YES")
    else:
        print("NO")
