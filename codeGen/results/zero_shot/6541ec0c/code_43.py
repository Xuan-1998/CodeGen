import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    visited = [False] * n
    components = []

    def dfs(node, value):
        visited[node] = True
        component = [value]
        stack = [(node, value)]
        while stack:
            node, value = stack.pop()
            for edge in edges:
                if edge[0] == node and not visited[edge[1]]:
                    stack.append((edge[1], value ^ values[edge[1]]))
                    visited[edge[1]] = True
                elif edge[1] == node and not visited[edge[0]]:
                    stack.append((edge[0], value ^ values[edge[0]]))
                    visited[edge[0]] = True
            if all(visited[i] for i in range(n)):
                break
        return component

    for i in range(n):
        if not visited[i]:
            components.append(dfs(i, values[i]))

    result = "YES" if len(set(map(frozenset, (component for component in components)))) == 1 else "NO"
    print(result)

if __name__ == "__main__":
    solve()
