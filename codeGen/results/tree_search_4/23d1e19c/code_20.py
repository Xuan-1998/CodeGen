def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u - 1, v - 1))

    s, t, path_length = map(int, input().split())
    path = list(map(int, input().split()))

    dp = {}
    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        if i == t:
            return 0
        min_recomputation = float('inf')
        for k in range(path_length + 1):
            next_j = path[k] - 1
            if edges[i][0] != j and edges[i][1] != j:
                recomputation = dfs(next_j, t) + 1
                min_recomputation = min(min_recomputation, recomputation)
        dp[(i, j)] = min_recomputation
        return dp[(i, j)]

    max_min_recomputation = float('-inf')
    max_max_recomputation = 0
    for i in range(len(path)):
        next_j = path[i] - 1
        if edges[path[i-1]][0] != next_j and edges[path[i-1]][1] != next_j:
            min_recomputation = dfs(next_j, t)
            max_max_recomputation = max(max_max_recomputation, min_recomputation)
            max_min_recomputation = min(max_min_recomputation, min_recomputation)

    print(min_recomputation, max_recomputation)

if __name__ == "__main__":
    main()
