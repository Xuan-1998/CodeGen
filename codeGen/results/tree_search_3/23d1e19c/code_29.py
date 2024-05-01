def min_max_recomputations(graph, path):
    n = len(graph)
    dp = [float('inf')] * (n + 1)
    memoization_dict = {}

    def dfs(vertex):
        if vertex == t:
            return 0
        if dp[vertex] != float('inf'):
            return dp[vertex]
        min_recomputations = float('inf')
        max_recomputations = 0

        for next_vertex in range(vertex + 1, n + 1):
            if has_edge(next_vertex, vertex):
                min_recomputations = min(min_recomputations, dfs(next_vertex) + 1)
                max_recomputations = max(max_recomputations, memoization_dict.get(next_vertex, float('inf')))

        dp[vertex] = min_recomputations
        return min_recomputations

    t = path[-1]
    for vertex in range(n):
        if has_edge(vertex, path[0]):
            break

    dfs(vertex)
    return dp[t], max(dp)

# Code to read input and print output
