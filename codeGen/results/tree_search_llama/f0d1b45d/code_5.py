def count_trees(p):
    n = len(p)
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)

    def dfs(u):
        if not visited[u]:
            visited[u] = True
            for v in range(1, n + 1):
                if p[v - 1] == u and parent[v] != -1:
                    parent[v] = u
                    dfs(v)
        return

    trees = 0
    for i in range(1, n + 1):
        if not visited[i]:
            trees += 1
            dfs(i)

    return trees

n = int(input())
p = list(map(int, input().split()))
print(count_trees(p))
