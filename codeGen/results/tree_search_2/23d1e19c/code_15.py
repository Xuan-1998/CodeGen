def min_max_recomputation(graph, s, t, p):
    memo = {}

    def dfs(v, count=0):
        if (v, count) in memo:
            return memo[(v, count)]

        if v == t:
            return 0, 0

        if graph[v] not in memo:
            min_recomputation, max_recomputation = float('inf'), 0
            for neighbor in graph[v]:
                if neighbor in p:
                    continue
                neighbor_count = dfs(neighbor, count + 1)
                min_recomputation = min(min_recomputation, neighbor_count[0] + (count == 0))
                max_recomputation = max(max_recomputation, neighbor_count[1] + (count == 0))

            memo[(v, count)] = min_recomputation, max_recomputation
        else:
            memo[(v, count)] = memo[(v, count)]

        return memo[(v, count)]

    return dfs(s)
