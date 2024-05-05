def solve():
    n = int(input())
    roads = [list(map(int, input().split())) for _ in range(n-1)]

    # First, let's find the root of each connected component
    parent = list(range(1, n+1))
    def find(x):
        if parent[x-1] != x:
            parent[x-1] = find(parent[x-1])
        return parent[x-1]

    for si, ti in roads:
        parent[ti-1] = si

    # Now let's count the number of children each node has
    degree = [0] * n
    def dfs(x):
        degree[x-1] += 1
        for child in range(1, n+1):
            if find(child) == x:
                dfs(child)

    for x in range(2, n+1):
        dfs(find(x))

    # The capital city is the node with the minimum out-degree
    min_degree = min(degree[1:])
    capitals = [i+1 for i, d in enumerate(degree[1:]) if d == min_degree]

    print(min_degree)
    print(' '.join(map(str, capitals)))

if __name__ == "__main__":
    solve()
